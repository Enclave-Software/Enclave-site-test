# Copy the CSS file to static directory
import shutil

# Copy the existing CSS file
try:
    shutil.copy('static/messenger-style.css', 'static/messenger-style.css')
    print("✅ CSS file already exists in static directory")
except:
    # If it doesn't exist, create a minimal version
    minimal_css = '''/* Simplified CSS for Vercel deployment - using existing design system */
@import url("data:text/css,''' + open('static/messenger-style.css', 'r').read().replace('\n', '\\A').replace('"', '\\"') + '''");
'''
    
    with open('static/messenger-style.css', 'w') as f:
        with open('static/messenger-style.css', 'r') as source:
            f.write(source.read())
    print("✅ CSS file copied to static directory")

# Create a deployment README
deployment_readme = '''# Enclave Messenger - Vercel Deployment

This is the Vercel-compatible version of Enclave Messenger.

## 🚀 Deploy to Vercel

### Method 1: Deploy Button
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/your-username/enclave-messenger)

### Method 2: Vercel CLI

1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Deploy**:
   ```bash
   vercel
   ```

3. **Set Environment Variables**:
   ```bash
   vercel env add SECRET_KEY
   # Enter a random secret key when prompted
   ```

### Method 3: GitHub Integration

1. Push this code to a GitHub repository
2. Connect your repository to Vercel
3. Deploy automatically on every push

## 📁 File Structure

```
enclave-messenger-vercel/
├── api/
│   └── index.py          # Main Flask application (serverless function)
├── static/
│   ├── messenger-style.css  # Styling
│   └── messenger-vercel.js  # Client-side JavaScript (HTTP-based)
├── templates/
│   ├── login.html        # Login page
│   └── messenger.html    # Main messenger interface
├── vercel.json          # Vercel configuration
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## ⚠️ Limitations on Vercel

Since Vercel is a serverless platform, this version has some limitations compared to the full desktop application:

### What Works:
- ✅ User authentication and profiles
- ✅ User search and discovery
- ✅ Sending and receiving messages
- ✅ Conversation history
- ✅ Modern responsive UI
- ✅ Basic security features

### What's Different:
- ❌ **No Real-time WebSockets**: Uses HTTP polling instead
- ❌ **No Persistent Database**: Uses in-memory storage (resets on deployment)
- ❌ **No End-to-End Encryption**: Simplified for demo purposes
- ❌ **Limited Session Persistence**: Sessions may not persist between deployments

## 🔧 Configuration

### Environment Variables

Set these in your Vercel dashboard:

- `SECRET_KEY`: A random secret key for Flask sessions

### For Production Use

To make this production-ready, consider:

1. **Database**: Replace in-memory storage with:
   - Vercel KV (Redis)
   - Supabase (PostgreSQL)
   - PlanetScale (MySQL)
   - MongoDB Atlas

2. **Real-time Features**: Add WebSocket support via:
   - Pusher
   - Ably
   - Socket.IO with external hosting
   - Vercel Edge Functions (limited WebSocket support)

3. **Encryption**: Implement proper end-to-end encryption:
   - Use Web Crypto API
   - Integrate with the existing secure_messenger.py logic
   - Store encrypted keys securely

## 🔒 Security Notes

This Vercel version is a **demo/prototype**. For production use:

- Implement proper authentication
- Add rate limiting
- Use HTTPS (Vercel provides this automatically)
- Implement proper session management
- Add input validation and sanitization
- Use a real database with proper security

## 🚀 Making it Production Ready

Here's what you'd need to add for a full production deployment:

### 1. Database Integration
```python
# Example with Vercel KV
import os
from redis import Redis

redis_client = Redis.from_url(os.environ.get('KV_URL'))
```

### 2. Real-time Features
```javascript
// Example with Pusher
const pusher = new Pusher(process.env.PUSHER_KEY, {
    cluster: process.env.PUSHER_CLUSTER
});
```

### 3. Authentication
```python
# Example with proper session management
from flask_session import Session
import redis

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.from_url(os.environ.get('REDIS_URL'))
```

## 📞 Support

For the full-featured version with real-time WebSockets and end-to-end encryption, use the desktop application included in this repository.
'''

with open('README-VERCEL.md', 'w') as f:
    f.write(deployment_readme)

print("✅ Created Vercel deployment README")

# Create a simple package.json for easier deployment
package_json = '''{
  "name": "enclave-messenger-vercel",
  "version": "1.0.0",
  "description": "Secure messaging application for Vercel",
  "scripts": {
    "dev": "vercel dev",
    "build": "echo 'No build step needed'",
    "deploy": "vercel --prod"
  },
  "keywords": ["messaging", "encryption", "privacy", "vercel"],
  "author": "Enclave Messenger Team",
  "license": "MIT"
}'''

with open('package.json', 'w') as f:
    f.write(package_json)

print("✅ Created package.json for easier deployment")