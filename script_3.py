# Create requirements.txt for Vercel
requirements = '''Flask==2.3.3
python-dotenv==1.0.0
'''

with open('requirements.txt', 'w') as f:
    f.write(requirements)

print("✅ Created requirements.txt for Vercel")

# Create a simplified messenger template for Vercel (without WebSocket)
messenger_template_vercel = '''<!DOCTYPE html>
<html lang="en" data-username="{{ username }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enclave Messenger</title>
    <link rel="stylesheet" href="/static/messenger-style.css">
</head>
<body class="messenger-page">
    <div class="messenger-container">
        <!-- Sidebar -->
        <div class="messenger-sidebar">
            <div class="sidebar-header">
                <div class="user-profile">
                    <div class="avatar">
                        <span id="userAvatar">{{ username[0].upper() if username else 'U' }}</span>
                        <div class="status-indicator online"></div>
                    </div>
                    <div class="user-info">
                        <h3 id="userDisplayName">{{ username or 'Guest' }}</h3>
                        <p id="userStatus">Online</p>
                    </div>
                </div>
                
                <div class="sidebar-actions">
                    <button class="btn-icon" id="newChatBtn" title="New Chat">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm5 11h-4v4h-2v-4H7v-2h4V7h2v4h4v2z"/>
                        </svg>
                    </button>
                    <button class="btn-icon" id="refreshBtn" title="Refresh">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M17.65 6.35C16.2 4.9 14.21 4 12 4c-4.42 0-7.99 3.58-7.99 8s3.57 8 7.99 8c3.73 0 6.84-2.55 7.73-6h-2.08c-.82 2.33-3.04 4-5.65 4-3.31 0-6-2.69-6-6s2.69-6 6-6c1.66 0 3.14.69 4.22 1.78L13 11h7V4l-2.35 2.35z"/>
                        </svg>
                    </button>
                </div>
            </div>
            
            <div class="search-container">
                <div class="search-box">
                    <svg class="search-icon" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
                    </svg>
                    <input type="text" id="searchInput" placeholder="Search people..." class="search-input">
                </div>
                <div id="searchResults" class="search-results hidden"></div>
            </div>
            
            <div class="conversations-container">
                <div class="conversations-header">
                    <h3>Messages</h3>
                </div>
                
                <div id="conversationsList" class="conversations-list">
                    <!-- Conversations will be populated here -->
                </div>
            </div>
        </div>
        
        <!-- Main Chat Area -->
        <div class="chat-main">
            <div id="welcomeView" class="welcome-view">
                <div class="welcome-content">
                    <div class="welcome-icon">💬</div>
                    <h2>Welcome to Enclave Messenger</h2>
                    <p>Search for people and start secure conversations.</p>
                    <p><small>⚠️ Note: This is a demo version. For full real-time features, use the desktop application.</small></p>
                    
                    <div class="quick-actions">
                        <button class="btn btn--primary" id="quickNewChat">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M20 2H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h4v3c0 .6.4 1 1 1h.5c.2 0 .4-.1.6-.2L12 19h8c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-3 12H7v-2h10v2zm0-3H7V9h10v2zm0-3H7V6h10v2z"/>
                            </svg>
                            Find People
                        </button>
                    </div>
                </div>
            </div>
            
            <div id="chatView" class="chat-view hidden">
                <div class="chat-header">
                    <div class="chat-header-info">
                        <div class="chat-avatar">
                            <span id="chatAvatar"></span>
                            <div id="chatStatus" class="status-indicator"></div>
                        </div>
                        <div class="chat-details">
                            <h3 id="chatTitle"></h3>
                            <p id="chatSubtitle"></p>
                        </div>
                    </div>
                    
                    <div class="chat-header-actions">
                        <button class="btn-icon" id="refreshMessagesBtn" title="Refresh Messages">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M17.65 6.35C16.2 4.9 14.21 4 12 4c-4.42 0-7.99 3.58-7.99 8s3.57 8 7.99 8c3.73 0 6.84-2.55 7.73-6h-2.08c-.82 2.33-3.04 4-5.65 4-3.31 0-6-2.69-6-6s2.69-6 6-6c1.66 0 3.14.69 4.22 1.78L13 11h7V4l-2.35 2.35z"/>
                            </svg>
                        </button>
                    </div>
                </div>
                
                <div class="messages-container" id="messagesContainer">
                    <div id="messagesList" class="messages-list">
                        <!-- Messages will be populated here -->
                    </div>
                </div>
                
                <div class="message-composer">
                    <div class="message-input-container">
                        <input type="text" id="messageInput" class="message-input" placeholder="Type a message...">
                        <button class="btn-icon send-btn" id="sendBtn" title="Send Message">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/>
                            </svg>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Modals -->
    <div id="newChatModal" class="modal hidden">
        <div class="modal-backdrop"></div>
        <div class="modal-content">
            <div class="modal-header">
                <h3>Find People</h3>
                <button class="btn-icon modal-close">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
                    </svg>
                </button>
            </div>
            <div class="modal-body">
                <div class="search-box">
                    <input type="text" id="userSearchInput" placeholder="Search for people..." class="form-control">
                </div>
                <div id="userSearchResults" class="user-search-results"></div>
            </div>
        </div>
    </div>

    <!-- Scripts -->
    <script>
        // Pass username to JavaScript
        window.username = "{{ username }}";
    </script>
    <script src="/static/messenger-vercel.js"></script>
</body>
</html>'''

with open('templates/messenger.html', 'w') as f:
    f.write(messenger_template_vercel)

print("✅ Created Vercel-compatible messenger template")