from flask import Flask, render_template, request, jsonify, session
import os
import json
import time
import secrets
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', secrets.token_hex(16))

# Simple in-memory storage for demo purposes
# In production, replace with Vercel KV, Supabase, or another database
class SimpleStorage:
    def __init__(self):
        self.users = {}
        self.groups = {}
        self.messages = []

    def create_user(self, username, display_name, email=None, bio=None):
        if username in self.users:
            return False

        self.users[username] = {
            'username': username,
            'display_name': display_name,
            'email': email,
            'bio': bio,
            'status': 'offline',
            'created_at': time.time(),
            'last_seen': time.time()
        }
        return True

    def get_user(self, username):
        return self.users.get(username)

    def search_users(self, query, limit=10):
        results = []
        for user in self.users.values():
            if query.lower() in user['username'].lower() or query.lower() in user['display_name'].lower():
                results.append({
                    'username': user['username'],
                    'display_name': user['display_name'],
                    'status': user['status'],
                    'bio': user.get('bio', '')
                })
        return results[:limit]

    def add_message(self, sender, recipient, content, message_type='text'):
        message = {
            'id': secrets.token_hex(8),
            'sender': sender,
            'recipient': recipient,
            'content': content,
            'type': message_type,
            'timestamp': time.time()
        }
        self.messages.append(message)
        return message

    def get_messages(self, user1, user2, limit=50):
        conversation = []
        for msg in self.messages:
            if ((msg['sender'] == user1 and msg['recipient'] == user2) or 
                (msg['sender'] == user2 and msg['recipient'] == user1)):
                conversation.append(msg)

        # Sort by timestamp and return most recent
        conversation.sort(key=lambda x: x['timestamp'])
        return conversation[-limit:]

# Initialize storage
storage = SimpleStorage()

@app.route('/')
def index():
    """Main messenger interface"""
    username = session.get('username', '')
    if not username:
        return render_template('login.html')
    return render_template('messenger.html', username=username)

@app.route('/login')
def login():
    """Login page"""
    return render_template('login.html')

@app.route('/api/login', methods=['POST'])
def api_login():
    """Handle login"""
    try:
        data = request.json
        username = data.get('username', '').strip()
        display_name = data.get('display_name', username).strip()

        if not username:
            return jsonify({'success': False, 'message': 'Username required'})

        # Get or create user
        user = storage.get_user(username)
        if not user:
            if storage.create_user(username, display_name):
                user = storage.get_user(username)
            else:
                return jsonify({'success': False, 'message': 'Failed to create user'})

        session['username'] = username
        return jsonify({'success': True, 'user': user})

    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'})

@app.route('/api/search/users')
def search_users():
    """Search for users"""
    try:
        query = request.args.get('q', '')
        if len(query) < 2:
            return jsonify({'users': []})

        users_list = storage.search_users(query)
        return jsonify({'users': users_list})

    except Exception as e:
        return jsonify({'users': [], 'error': str(e)})

@app.route('/api/messages', methods=['GET', 'POST'])
def handle_messages():
    """Handle message sending and retrieval"""
    if 'username' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'})

    if request.method == 'POST':
        try:
            data = request.json
            sender = session['username']
            recipient = data.get('recipient')
            content = data.get('content', '').strip()

            if not recipient or not content:
                return jsonify({'success': False, 'message': 'Recipient and content required'})

            message = storage.add_message(sender, recipient, content)
            return jsonify({'success': True, 'message': message})

        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})

    else:  # GET
        try:
            username = session['username']
            other_user = request.args.get('with')

            if other_user:
                messages = storage.get_messages(username, other_user)
                return jsonify({'messages': messages})
            else:
                return jsonify({'messages': []})

        except Exception as e:
            return jsonify({'messages': [], 'error': str(e)})

@app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': time.time(),
        'message': 'Enclave Messenger API is running on Vercel',
        'users_count': len(storage.users),
        'messages_count': len(storage.messages)
    })

# This is the entry point for Vercel
app_handler = app

if __name__ == '__main__':
    app.run(debug=True)
