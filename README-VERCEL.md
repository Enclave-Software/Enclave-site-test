# Enclave Messenger - Vercel Deployment

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
