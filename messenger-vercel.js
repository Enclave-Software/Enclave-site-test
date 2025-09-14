// Enclave Messenger Web - Vercel Compatible (HTTP-based)
class EnclaveMessengerClient {
    constructor() {
        this.currentUser = null;
        self.activeConversation = null;
        this.conversations = new Map();
        this.users = new Map();
        this.pollInterval = null;

        this.init();
    }

    init() {
        // Get current user from page context
        this.currentUser = document.documentElement.dataset.username || window.username;

        this.setupUIEvents();

        if (this.currentUser) {
            this.updateUserProfile({ username: this.currentUser, display_name: this.currentUser });
            this.startPolling();
        }
    }

    setupUIEvents() {
        // Search functionality
        const searchInput = document.getElementById('searchInput');
        const userSearchInput = document.getElementById('userSearchInput');

        if (searchInput) {
            searchInput.addEventListener('input', (e) => {
                this.handleSearch(e.target.value);
            });
        }

        if (userSearchInput) {
            userSearchInput.addEventListener('input', (e) => {
                this.searchUsers(e.target.value);
            });
        }

        // New chat button
        const newChatBtn = document.getElementById('newChatBtn');
        const quickNewChat = document.getElementById('quickNewChat');
        if (newChatBtn) newChatBtn.addEventListener('click', () => this.showNewChatModal());
        if (quickNewChat) quickNewChat.addEventListener('click', () => this.showNewChatModal());

        // Refresh button
        const refreshBtn = document.getElementById('refreshBtn');
        if (refreshBtn) refreshBtn.addEventListener('click', () => this.refreshData());

        // Message input
        const messageInput = document.getElementById('messageInput');
        if (messageInput) {
            messageInput.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    this.sendMessage();
                }
            });
        }

        // Send button
        const sendBtn = document.getElementById('sendBtn');
        if (sendBtn) {
            sendBtn.addEventListener('click', () => this.sendMessage());
        }

        // Refresh messages button
        const refreshMessagesBtn = document.getElementById('refreshMessagesBtn');
        if (refreshMessagesBtn) {
            refreshMessagesBtn.addEventListener('click', () => this.loadMessages());
        }

        // Modal events
        this.setupModalEvents();
    }

    setupModalEvents() {
        // Modal close buttons
        document.querySelectorAll('.modal-close, .modal-backdrop').forEach(el => {
            el.addEventListener('click', (e) => {
                if (e.target === el) {
                    this.closeModals();
                }
            });
        });

        // Escape key to close modals
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                this.closeModals();
            }
        });
    }

    startPolling() {
        // Poll for updates every 5 seconds (since we don't have WebSocket on Vercel)
        this.pollInterval = setInterval(() => {
            if (this.activeConversation) {
                this.loadMessages();
            }
        }, 5000);
    }

    stopPolling() {
        if (this.pollInterval) {
            clearInterval(this.pollInterval);
            this.pollInterval = null;
        }
    }

    updateUserProfile(profile) {
        const avatarEl = document.getElementById('userAvatar');
        const displayNameEl = document.getElementById('userDisplayName');

        if (avatarEl && profile.username) {
            avatarEl.textContent = profile.display_name?.[0]?.toUpperCase() || profile.username[0].toUpperCase();
        }

        if (displayNameEl) {
            displayNameEl.textContent = profile.display_name || profile.username;
        }
    }

    async handleSearch(query) {
        if (query.length >= 2) {
            await this.searchUsers(query);
        } else {
            this.hideSearchResults();
        }
    }

    async searchUsers(query) {
        if (query.length < 2) {
            document.getElementById('userSearchResults').innerHTML = '';
            return;
        }

        try {
            const response = await fetch(`/api/search/users?q=${encodeURIComponent(query)}`);
            const data = await response.json();
            this.displayUserSearchResults(data.users || []);
        } catch (error) {
            console.error('User search error:', error);
            this.showError('Failed to search users');
        }
    }

    displayUserSearchResults(users) {
        const resultsContainer = document.getElementById('userSearchResults');
        if (!resultsContainer) return;

        resultsContainer.innerHTML = '';

        if (users.length === 0) {
            resultsContainer.innerHTML = '<div class="no-results">No users found</div>';
            return;
        }

        users.forEach(user => {
            if (user.username === this.currentUser) return; // Skip self

            const userEl = document.createElement('div');
            userEl.className = 'user-result-item';

            userEl.innerHTML = `
                <div class="user-result-avatar">${user.display_name?.[0]?.toUpperCase() || user.username[0].toUpperCase()}</div>
                <div class="user-result-info">
                    <h4>${user.display_name || user.username}</h4>
                    <p>@${user.username}</p>
                </div>
            `;

            userEl.addEventListener('click', () => {
                this.startChatWithUser(user);
            });

            resultsContainer.appendChild(userEl);
        });
    }

    startChatWithUser(user) {
        const conversationId = `dm_${user.username}`;

        // Check if conversation already exists
        if (this.conversations.has(conversationId)) {
            this.openConversation(this.conversations.get(conversationId));
        } else {
            // Create new DM conversation
            const conversation = {
                id: conversationId,
                name: user.display_name || user.username,
                type: 'dm',
                recipient: user.username,
                lastMessage: 'No messages yet',
                time: 'Now',
                unread: 0,
                avatar: user.display_name?.[0]?.toUpperCase() || user.username[0].toUpperCase(),
                status: user.status || 'offline'
            };

            this.addConversationToList(conversation);
            this.openConversation(conversation);
        }

        this.closeModals();
    }

    addConversationToList(conversation) {
        const conversationsList = document.getElementById('conversationsList');
        if (!conversationsList) return;

        const conversationEl = document.createElement('div');
        conversationEl.className = 'conversation-item';
        conversationEl.dataset.conversationId = conversation.id;

        conversationEl.innerHTML = `
            <div class="avatar">
                <span>${conversation.avatar}</span>
                <div class="status-indicator ${conversation.status || 'offline'}"></div>
            </div>
            <div class="conversation-info">
                <h4 class="conversation-name">${conversation.name}</h4>
                <p class="conversation-preview">${conversation.lastMessage}</p>
            </div>
            <div class="conversation-meta">
                <span class="conversation-time">${conversation.time}</span>
                ${conversation.unread > 0 ? `<span class="unread-badge">${conversation.unread}</span>` : ''}
            </div>
        `;

        conversationEl.addEventListener('click', () => {
            this.openConversation(conversation);
        });

        conversationsList.appendChild(conversationEl);
        this.conversations.set(conversation.id, conversation);
    }

    openConversation(conversation) {
        // Update active conversation
        this.activeConversation = conversation;

        // Update UI
        document.querySelectorAll('.conversation-item').forEach(el => {
            el.classList.remove('active');
        });

        const conversationEl = document.querySelector(`[data-conversation-id="${conversation.id}"]`);
        if (conversationEl) {
            conversationEl.classList.add('active');
        }

        // Show chat view
        document.getElementById('welcomeView').classList.add('hidden');
        document.getElementById('chatView').classList.remove('hidden');

        // Update chat header
        const chatTitle = document.getElementById('chatTitle');
        const chatSubtitle = document.getElementById('chatSubtitle');
        const chatAvatar = document.getElementById('chatAvatar');

        if (chatTitle) chatTitle.textContent = conversation.name;
        if (chatSubtitle) {
            chatSubtitle.textContent = conversation.type === 'group' ? 
                `Group • ${conversation.memberCount || 0} members` : 
                'Direct message';
        }
        if (chatAvatar) chatAvatar.textContent = conversation.avatar;

        // Load messages
        this.loadMessages();
    }

    async loadMessages() {
        if (!this.activeConversation || !this.activeConversation.recipient) return;

        try {
            const response = await fetch(`/api/messages?with=${encodeURIComponent(this.activeConversation.recipient)}`);
            const data = await response.json();

            if (data.messages) {
                this.displayMessages(data.messages);
            }
        } catch (error) {
            console.error('Failed to load messages:', error);
        }
    }

    displayMessages(messages) {
        const messagesList = document.getElementById('messagesList');
        if (!messagesList) return;

        messagesList.innerHTML = '';

        messages.forEach(message => {
            this.displayMessage(message);
        });

        messagesList.scrollTop = messagesList.scrollHeight;
    }

    displayMessage(messageData) {
        const messagesList = document.getElementById('messagesList');
        if (!messagesList) return;

        const messageEl = document.createElement('div');
        messageEl.className = `message ${messageData.sender === this.currentUser ? 'own' : ''}`;

        const isOwn = messageData.sender === this.currentUser;
        const avatar = messageData.sender[0].toUpperCase();
        const timestamp = new Date(messageData.timestamp * 1000).toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});

        messageEl.innerHTML = `
            ${!isOwn ? `<div class="message-avatar">${avatar}</div>` : ''}
            <div class="message-content">
                ${this.escapeHtml(messageData.content)}
                <div class="message-time">${timestamp}</div>
            </div>
            ${isOwn ? `<div class="message-avatar">${this.currentUser[0].toUpperCase()}</div>` : ''}
        `;

        messagesList.appendChild(messageEl);
        messagesList.scrollTop = messagesList.scrollHeight;
    }

    async sendMessage() {
        const messageInput = document.getElementById('messageInput');
        if (!messageInput || !this.activeConversation) return;

        const content = messageInput.value.trim();
        if (!content) return;

        try {
            const response = await fetch('/api/messages', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    recipient: this.activeConversation.recipient,
                    content: content
                })
            });

            const result = await response.json();

            if (result.success) {
                // Clear input
                messageInput.value = '';

                // Immediately show the sent message
                this.displayMessage({
                    sender: this.currentUser,
                    content: content,
                    timestamp: Date.now() / 1000
                });

                // Update conversation preview
                this.updateConversationPreview(this.activeConversation.id, {
                    sender: this.currentUser,
                    content: content,
                    timestamp: Date.now() / 1000
                });
            } else {
                this.showError(result.message || 'Failed to send message');
            }
        } catch (error) {
            console.error('Send message error:', error);
            this.showError('Failed to send message');
        }
    }

    updateConversationPreview(conversationId, messageData) {
        const conversationEl = document.querySelector(`[data-conversation-id="${conversationId}"]`);
        if (conversationEl) {
            const previewEl = conversationEl.querySelector('.conversation-preview');
            const timeEl = conversationEl.querySelector('.conversation-time');

            if (previewEl) {
                const preview = messageData.sender === this.currentUser ? 
                    `You: ${messageData.content}` : 
                    messageData.content;
                previewEl.textContent = this.truncateText(preview, 40);
            }

            if (timeEl) {
                timeEl.textContent = 'Now';
            }
        }
    }

    refreshData() {
        if (this.activeConversation) {
            this.loadMessages();
        }
        this.showInfo('Data refreshed');
    }

    showNewChatModal() {
        document.getElementById('newChatModal').classList.remove('hidden');
        document.getElementById('userSearchInput').focus();
    }

    closeModals() {
        document.querySelectorAll('.modal').forEach(modal => {
            modal.classList.add('hidden');
        });

        // Clear search results
        const userSearchResults = document.getElementById('userSearchResults');
        if (userSearchResults) {
            userSearchResults.innerHTML = '';
        }

        // Clear search input
        const userSearchInput = document.getElementById('userSearchInput');
        if (userSearchInput) {
            userSearchInput.value = '';
        }
    }

    hideSearchResults() {
        const searchResults = document.getElementById('searchResults');
        if (searchResults) {
            searchResults.classList.add('hidden');
        }
    }

    showError(message) {
        this.showToast(message, 'error');
    }

    showInfo(message) {
        this.showToast(message, 'info');
    }

    showToast(message, type = 'info') {
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        toast.textContent = message;
        toast.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${type === 'error' ? 'var(--color-error)' : 'var(--color-primary)'};
            color: white;
            padding: 12px 16px;
            border-radius: 8px;
            z-index: 2000;
            animation: slideInRight 0.3s ease;
        `;

        document.body.appendChild(toast);

        setTimeout(() => {
            toast.remove();
        }, 3000);
    }

    // Utility functions
    truncateText(text, maxLength) {
        return text.length > maxLength ? text.substring(0, maxLength) + '...' : text;
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    destroy() {
        this.stopPolling();
    }
}

// Initialize the messenger when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // Get username from the template context or page
    const htmlEl = document.documentElement;
    if (htmlEl.dataset.username) {
        window.username = htmlEl.dataset.username;
    }

    // Initialize messenger client
    if (window.username) {
        window.messenger = new EnclaveMessengerClient();
    }
});

// Clean up on page unload
window.addEventListener('beforeunload', () => {
    if (window.messenger) {
        window.messenger.destroy();
    }
});

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }

    .toast {
        animation: slideInRight 0.3s ease;
    }

    .no-results {
        padding: 20px;
        text-align: center;
        color: var(--color-text-secondary);
        font-style: italic;
    }

    .vercel-info {
        margin-top: 20px;
        padding: 12px;
        background: rgba(var(--color-primary), 0.1);
        border-radius: var(--radius-base);
    }

    .vercel-info small {
        color: var(--color-text-secondary);
        line-height: 1.4;
    }
`;
document.head.appendChild(style);
