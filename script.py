# Create the Vercel-compatible structure
# Note: Vercel has limitations with WebSockets and SQLite, so we'll need to adapt

# 1. Create the main API handler for Vercel
vercel_api_handler = '''from flask import Flask, render_template, request, jsonify, session
import os
import json
import time
import secrets
from datetime import datetime

# Import our secure messenger (we'll need to adapt this for serverless)
# from secure_messenger import SecureMessenger

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', secrets.token_hex(16))

# Global state - Note: This won't persist between serverless function calls
# For production, you'd want to use a database like Vercel KV or Supabase
users = {}
groups = {}

# Simple in-memory storage for demo purposes
# In production, replace with a proper database
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

# Initialize simple storage
storage = SimpleStorage()

@app.route('/')
def index():
    """Main messenger interface"""
    return render_template('messenger.html', username=session.get('username', ''))

@app.route('/login')
def login():
    """Login page"""
    return render_template('login.html')

@app.route('/api/login', methods=['POST'])
def api_login():
    """Handle login"""
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

@app.route('/api/search/users')
def search_users():
    """Search for users"""
    query = request.args.get('q', '')
    if len(query) < 2:
        return jsonify({'users': []})
    
    users_list = storage.search_users(query)
    return jsonify({'users': users_list})

@app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': time.time(),
        'message': 'Enclave Messenger API is running on Vercel'
    })

# Note: WebSocket functionality is limited on Vercel
# For real-time features, you'd need to use:
# 1. Vercel's Edge Functions with WebSockets (limited)
# 2. A separate WebSocket service (like Pusher, Ably, or Socket.IO hosted elsewhere)
# 3. Polling-based updates

if __name__ == '__main__':
    app.run(debug=True)
'''

# Save the API handler
with open('api/index.py', 'w') as f:
    f.write(vercel_api_handler)

print("✅ Created Vercel API handler: api/index.py")