# Let me copy the existing CSS content and create the necessary files
# First, let me read the original CSS content from our previous creation

# Copy the CSS file content from the existing file we created earlier
with open('static/messenger-style.css', 'w') as f:
    # Write a simplified version of the CSS for Vercel
    css_content = '''/* Enclave Messenger - Vercel Compatible CSS */
:root {
  /* Color tokens */
  --color-primary: #33808d;
  --color-primary-hover: #1d7480;
  --color-primary-active: #1a6873;
  --color-background: #fcfcf9;
  --color-surface: #fffffe;
  --color-text: #133c3b;
  --color-text-secondary: #626c71;
  --color-border: rgba(94, 82, 64, 0.2);
  --color-success: #33808d;
  --color-error: #c0152f;
  
  /* Spacing */
  --space-4: 4px;
  --space-8: 8px;
  --space-12: 12px;
  --space-16: 16px;
  --space-20: 20px;
  --space-24: 24px;
  --space-32: 32px;
  
  /* Border radius */
  --radius-sm: 6px;
  --radius-base: 8px;
  --radius-lg: 12px;
  --radius-full: 9999px;
  
  /* Typography */
  --font-family-base: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-size-sm: 12px;
  --font-size-base: 14px;
  --font-size-lg: 16px;
  --font-size-xl: 18px;
  --font-size-2xl: 20px;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  
  /* Animation */
  --duration-fast: 150ms;
  --duration-normal: 250ms;
  --ease-standard: cubic-bezier(0.16, 1, 0.3, 1);
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  :root {
    --color-background: #1f2121;
    --color-surface: #262828;
    --color-text: #f5f5f5;
    --color-text-secondary: rgba(167, 169, 169, 0.7);
    --color-primary: #32b8c6;
    --color-border: rgba(119, 124, 124, 0.3);
  }
}

/* Base styles */
* { box-sizing: border-box; }
body {
  margin: 0;
  padding: 0;
  font-family: var(--font-family-base);
  font-size: var(--font-size-base);
  line-height: 1.5;
  color: var(--color-text);
  background-color: var(--color-background);
}

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-8) var(--space-16);
  border-radius: var(--radius-base);
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-medium);
  cursor: pointer;
  transition: all var(--duration-normal) var(--ease-standard);
  border: none;
  text-decoration: none;
  gap: var(--space-8);
}

.btn--primary {
  background: var(--color-primary);
  color: white;
}

.btn--primary:hover {
  background: var(--color-primary-hover);
}

.btn--secondary {
  background: var(--color-surface);
  color: var(--color-text);
  border: 1px solid var(--color-border);
}

.btn--full-width {
  width: 100%;
}

.btn-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: var(--radius-full);
  background: transparent;
  border: none;
  color: var(--color-text-secondary);
  cursor: pointer;
  transition: all var(--duration-normal) var(--ease-standard);
}

.btn-icon:hover {
  background: var(--color-surface);
  color: var(--color-text);
}

/* Form elements */
.form-control {
  display: block;
  width: 100%;
  padding: var(--space-8) var(--space-12);
  font-size: var(--font-size-base);
  color: var(--color-text);
  background-color: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-base);
  transition: border-color var(--duration-fast) var(--ease-standard);
}

.form-control:focus {
  outline: none;
  border-color: var(--color-primary);
}

.form-label {
  display: block;
  margin-bottom: var(--space-4);
  font-weight: var(--font-weight-medium);
  font-size: var(--font-size-sm);
}

.form-group {
  margin-bottom: var(--space-16);
}

/* Login page */
.login-page {
  background: linear-gradient(135deg, #133c3b, #262828);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-16);
}

.login-container {
  width: 100%;
  max-width: 400px;
}

.login-card {
  background: var(--color-surface);
  border-radius: var(--radius-lg);
  overflow: hidden;
}

.login-header {
  padding: var(--space-32) var(--space-24) var(--space-24);
  text-align: center;
  background: linear-gradient(135deg, var(--color-primary), #2da6b4);
  color: white;
}

.login-header h1 {
  margin: 0 0 var(--space-8) 0;
  font-size: var(--font-size-2xl);
  font-weight: var(--font-weight-semibold);
}

.login-header p {
  margin: 0;
  font-size: var(--font-size-sm);
  opacity: 0.9;
}

.login-form {
  padding: var(--space-32) var(--space-24);
}

.login-form h2 {
  margin: 0 0 var(--space-8) 0;
  font-size: var(--font-size-xl);
  font-weight: var(--font-weight-semibold);
}

.login-form > p {
  margin: 0 0 var(--space-24) 0;
  color: var(--color-text-secondary);
}

.login-features {
  margin-top: var(--space-32);
  padding-top: var(--space-24);
  border-top: 1px solid var(--color-border);
}

.login-features h4 {
  margin: 0 0 var(--space-12) 0;
  color: var(--color-primary);
}

.login-features ul {
  margin: 0;
  padding: 0;
  list-style: none;
}

.login-features li {
  padding: var(--space-4) 0;
  font-size: var(--font-size-sm);
  color: var(--color-text-secondary);
}

.login-features li::before {
  content: "✓";
  color: var(--color-success);
  font-weight: var(--font-weight-semibold);
  margin-right: var(--space-8);
}

/* Messenger layout */
.messenger-page {
  height: 100vh;
  overflow: hidden;
}

.messenger-container {
  display: flex;
  height: 100vh;
  background: var(--color-background);
}

/* Sidebar */
.messenger-sidebar {
  width: 320px;
  background: var(--color-surface);
  border-right: 1px solid var(--color-border);
  display: flex;
  flex-direction: column;
}

.sidebar-header {
  padding: var(--space-16);
  border-bottom: 1px solid var(--color-border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.user-profile {
  display: flex;
  align-items: center;
  gap: var(--space-12);
}

.avatar {
  position: relative;
  width: 40px;
  height: 40px;
  border-radius: var(--radius-full);
  background: var(--color-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: var(--font-weight-semibold);
}

.status-indicator {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 12px;
  height: 12px;
  border-radius: var(--radius-full);
  border: 2px solid var(--color-surface);
}

.status-indicator.online {
  background: var(--color-success);
}

.status-indicator.offline {
  background: var(--color-text-secondary);
}

.user-info h3 {
  margin: 0;
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-semibold);
}

.user-info p {
  margin: 0;
  font-size: 11px;
  color: var(--color-text-secondary);
}

.sidebar-actions {
  display: flex;
  gap: var(--space-4);
}

/* Search */
.search-container {
  padding: var(--space-16);
  border-bottom: 1px solid var(--color-border);
}

.search-box {
  position: relative;
}

.search-icon {
  position: absolute;
  left: var(--space-12);
  top: 50%;
  transform: translateY(-50%);
  color: var(--color-text-secondary);
}

.search-input {
  width: 100%;
  padding: var(--space-8) var(--space-12) var(--space-8) var(--space-32);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-full);
  background: var(--color-background);
  font-size: var(--font-size-sm);
}

.search-results {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-base);
  max-height: 300px;
  overflow-y: auto;
  z-index: 10;
}

/* Conversations */
.conversations-container {
  flex: 1;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.conversations-header {
  padding: var(--space-16);
  border-bottom: 1px solid var(--color-border);
}

.conversations-header h3 {
  margin: 0;
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-semibold);
}

.conversations-list {
  flex: 1;
  overflow-y: auto;
}

.conversation-item {
  padding: var(--space-12) var(--space-16);
  display: flex;
  align-items: center;
  gap: var(--space-12);
  cursor: pointer;
  border-bottom: 1px solid var(--color-border);
  transition: background-color var(--duration-fast) var(--ease-standard);
}

.conversation-item:hover {
  background: var(--color-background);
}

.conversation-item.active {
  background: rgba(var(--color-primary), 0.1);
  border-left: 3px solid var(--color-primary);
}

.conversation-info {
  flex: 1;
  min-width: 0;
}

.conversation-name {
  margin: 0 0 var(--space-4) 0;
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-medium);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.conversation-preview {
  margin: 0;
  font-size: var(--font-size-sm);
  color: var(--color-text-secondary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.conversation-meta {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: var(--space-4);
}

.conversation-time {
  font-size: 11px;
  color: var(--color-text-secondary);
}

/* Chat main */
.chat-main {
  flex: 1;
  display: flex;
  flex-direction: column;
  background: var(--color-background);
}

/* Welcome view */
.welcome-view {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-32);
}

.welcome-content {
  text-align: center;
  max-width: 400px;
}

.welcome-icon {
  font-size: 4rem;
  margin-bottom: var(--space-24);
}

.welcome-content h2 {
  margin: 0 0 var(--space-12) 0;
  font-size: var(--font-size-2xl);
  font-weight: var(--font-weight-semibold);
}

.welcome-content p {
  margin: 0 0 var(--space-32) 0;
  color: var(--color-text-secondary);
}

.quick-actions {
  display: flex;
  flex-direction: column;
  gap: var(--space-12);
}

/* Chat view */
.chat-view {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.chat-header {
  padding: var(--space-16) var(--space-24);
  border-bottom: 1px solid var(--color-border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--color-surface);
}

.chat-header-info {
  display: flex;
  align-items: center;
  gap: var(--space-12);
}

.chat-avatar {
  position: relative;
  width: 40px;
  height: 40px;
  border-radius: var(--radius-full);
  background: var(--color-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: var(--font-weight-semibold);
}

.chat-details h3 {
  margin: 0 0 var(--space-4) 0;
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-semibold);
}

.chat-details p {
  margin: 0;
  font-size: 11px;
  color: var(--color-text-secondary);
}

.chat-header-actions {
  display: flex;
  gap: var(--space-8);
}

/* Messages */
.messages-container {
  flex: 1;
  overflow: hidden;
}

.messages-list {
  height: 100%;
  overflow-y: auto;
  padding: var(--space-16) var(--space-24);
  display: flex;
  flex-direction: column;
  gap: var(--space-8);
}

.message {
  display: flex;
  gap: var(--space-8);
  max-width: 70%;
  align-items: flex-end;
}

.message.own {
  align-self: flex-end;
  flex-direction: row-reverse;
}

.message-avatar {
  width: 28px;
  height: 28px;
  border-radius: var(--radius-full);
  background: var(--color-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 11px;
  font-weight: var(--font-weight-semibold);
  flex-shrink: 0;
}

.message-content {
  background: var(--color-surface);
  padding: var(--space-8) var(--space-12);
  border-radius: var(--radius-lg);
  font-size: var(--font-size-base);
  word-wrap: break-word;
}

.message.own .message-content {
  background: var(--color-primary);
  color: white;
}

.message-time {
  font-size: 11px;
  color: var(--color-text-secondary);
  margin-top: var(--space-4);
}

/* Message composer */
.message-composer {
  padding: var(--space-16) var(--space-24);
  border-top: 1px solid var(--color-border);
  background: var(--color-surface);
}

.message-input-container {
  display: flex;
  align-items: center;
  gap: var(--space-8);
}

.message-input {
  flex: 1;
  padding: var(--space-8) var(--space-12);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  background: var(--color-background);
  font-size: var(--font-size-base);
  resize: none;
}

.message-input:focus {
  outline: none;
  border-color: var(--color-primary);
}

.send-btn {
  background: var(--color-primary);
  color: white;
}

.send-btn:hover {
  background: var(--color-primary-hover);
}

/* Modals */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-16);
}

.modal-backdrop {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
}

.modal-content {
  position: relative;
  background: var(--color-surface);
  border-radius: var(--radius-lg);
  width: 100%;
  max-width: 500px;
  max-height: 80vh;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.modal-header {
  padding: var(--space-20) var(--space-24) var(--space-16);
  border-bottom: 1px solid var(--color-border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.modal-header h3 {
  margin: 0;
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-semibold);
}

.modal-body {
  padding: var(--space-24);
  flex: 1;
  overflow-y: auto;
}

/* User search results */
.user-search-results {
  margin-top: var(--space-16);
  max-height: 300px;
  overflow-y: auto;
}

.user-result-item {
  display: flex;
  align-items: center;
  gap: var(--space-12);
  padding: var(--space-12);
  border-radius: var(--radius-base);
  cursor: pointer;
  transition: background-color var(--duration-fast) var(--ease-standard);
}

.user-result-item:hover {
  background: var(--color-background);
}

.user-result-avatar {
  width: 40px;
  height: 40px;
  border-radius: var(--radius-full);
  background: var(--color-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: var(--font-weight-semibold);
}

.user-result-info h4 {
  margin: 0 0 var(--space-4) 0;
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-medium);
}

.user-result-info p {
  margin: 0;
  font-size: var(--font-size-sm);
  color: var(--color-text-secondary);
}

/* Utility classes */
.hidden {
  display: none !important;
}

/* Responsive */
@media (max-width: 768px) {
  .messenger-sidebar {
    width: 100%;
    max-width: 320px;
    position: absolute;
    top: 0;
    left: -100%;
    z-index: 100;
    transition: left var(--duration-normal) var(--ease-standard);
  }
  
  .messenger-sidebar.open {
    left: 0;
  }
  
  .chat-main {
    width: 100%;
  }
}

/* Scrollbar styling */
.messages-list::-webkit-scrollbar,
.conversations-list::-webkit-scrollbar {
  width: 6px;
}

.messages-list::-webkit-scrollbar-track,
.conversations-list::-webkit-scrollbar-track {
  background: transparent;
}

.messages-list::-webkit-scrollbar-thumb,
.conversations-list::-webkit-scrollbar-thumb {
  background: var(--color-border);
  border-radius: var(--radius-full);
}
'''
    f.write(css_content)

print("✅ Created simplified CSS for Vercel")

# Create the deployment README
deployment_readme = '''# Enclave Messenger - Vercel Deployment

Deploy this secure messaging application to Vercel in minutes!

## 🚀 Quick Deploy

### One-Click Deploy
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=YOUR_GITHUB_URL)

### Manual Deployment

1. **Upload these files to your repository**
2. **Connect to Vercel**:
   - Go to [vercel.com](https://vercel.com)
   - Import your GitHub repository
   - Deploy automatically

3. **Set Environment Variables** (optional):
   ```
   SECRET_KEY=your_random_secret_key_here
   ```

## 📁 Files for Vercel

Here are all the files you need to upload:

```
your-repository/
├── api/
│   └── index.py              # Backend API (serverless function)
├── static/
│   ├── messenger-style.css   # Styling
│   └── messenger-vercel.js   # Frontend JavaScript
├── templates/
│   ├── login.html           # Login page
│   └── messenger.html       # Main messenger interface
├── vercel.json              # Vercel configuration
├── requirements.txt         # Python dependencies
├── package.json            # Node.js metadata
└── README-VERCEL.md        # This file
```

## ⚠️ Important Notes

This is a **demo version** with some limitations:

### ✅ What Works:
- User login and profiles
- Search for other users
- Send and receive messages
- Conversation history
- Responsive mobile-friendly design
- Modern, secure UI

### ❌ Limitations:
- **No real-time messaging** (uses refresh instead of WebSocket)
- **No persistent database** (data resets on new deployments)
- **Simplified encryption** (not the full end-to-end encryption)
- **In-memory storage** (sessions may not persist)

### 🔧 For Production Use

To make this production-ready, you would need:

1. **Real Database**: Replace in-memory storage with:
   - Vercel KV (Redis)
   - Supabase
   - PlanetScale
   - MongoDB Atlas

2. **Real-time Features**: Add WebSocket support via:
   - Pusher
   - Ably
   - Socket.IO (separate hosting)

3. **Proper Authentication**: Implement secure user management

## 🌐 Live Demo

Once deployed, your app will be available at:
```
https://your-app-name.vercel.app
```

## 🔧 Local Development

To test locally:

1. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Run locally**:
   ```bash
   vercel dev
   ```

3. **Open**: http://localhost:3000

## 🎯 Usage

1. **Visit your deployed site**
2. **Enter a username** (any name you want)
3. **Start messaging**:
   - Search for other users
   - Click "Find People" to discover others
   - Start conversations
   - Send messages

## 🔒 Security

This demo version includes:
- ✅ HTTPS (provided by Vercel)
- ✅ Input validation
- ✅ Session management
- ✅ Modern security headers
- ❌ End-to-end encryption (simplified for demo)

## 🚀 Upgrading to Full Version

For the complete Enclave Messenger experience with:
- Real-time WebSocket messaging
- Full end-to-end encryption
- Persistent database
- File sharing
- Voice/video calls

Download the desktop application from the main repository.

## 📞 Support

- **Issues**: Check the console for any errors
- **Updates**: Redeploy to get the latest version
- **Community**: Join our discussions for help

---

**Made with ❤️ for secure communication**
'''

with open('README-VERCEL.md', 'w') as f:
    f.write(deployment_readme)

print("✅ Created comprehensive Vercel deployment guide")

# Create package.json
package_json = '''{
  "name": "enclave-messenger-vercel",
  "version": "1.0.0",
  "description": "Secure messaging application deployed on Vercel",
  "main": "api/index.py",
  "scripts": {
    "dev": "vercel dev",
    "build": "echo 'No build step required for Python'",
    "deploy": "vercel --prod"
  },
  "keywords": [
    "messaging",
    "encryption",
    "privacy",
    "secure-chat",
    "vercel",
    "flask"
  ],
  "author": "Enclave Messenger Team",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/your-username/enclave-messenger"
  }
}'''

with open('package.json', 'w') as f:
    f.write(package_json)

print("✅ Created package.json for npm/yarn compatibility")