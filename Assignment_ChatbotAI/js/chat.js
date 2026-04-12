$(document).ready(function () {
    // --- Elements ---
    const $chatInput = $('#chat-input');
    const $sendBtn = $('#send-btn');
    const $messagesArea = $('#messages-area');
    const $welcomeSection = $('#welcome-section');

    // --- Part 4: Sidebar & Unified Toggle ---
    const $sidebar = $('#chat-sidebar');
    const $toggleBtn = $('#mobile-menu-btn');      // hamburger in main header
    const $sidebarCloseBtn = $('#sidebar-close-btn'); // chevron inside sidebar

    // Dynamically add the overlay to the body (used on mobile)
    $('body').append('<div class="sidebar-overlay" id="sidebar-overlay"></div>');
    const $overlay = $('#sidebar-overlay');

    function isMobile() {
        return window.innerWidth < 768;
    }

    function openSidebar() {
        if (isMobile()) {
            $sidebar.addClass('show').removeClass('collapsed');
            $overlay.addClass('show');
        } else {
            $sidebar.removeClass('collapsed');
        }
        $toggleBtn.find('i').removeClass('fa-bars').addClass('fa-bars-staggered');
    }

    function closeSidebar() {
        if (isMobile()) {
            $sidebar.removeClass('show');
            $overlay.removeClass('show');
        } else {
            $sidebar.addClass('collapsed');
        }
        $toggleBtn.find('i').removeClass('fa-bars-staggered').addClass('fa-bars');
    }

    function toggleSidebar() {
        const isOpen = isMobile() ? $sidebar.hasClass('show') : !$sidebar.hasClass('collapsed');
        if (isOpen) {
            closeSidebar();
        } else {
            openSidebar();
        }
    }

    $toggleBtn.on('click', toggleSidebar);
    $sidebarCloseBtn.on('click', closeSidebar);

    // Close via overlay tap (mobile)
    $overlay.on('click', closeSidebar);

    // Close sidebar automatically when window widens past mobile break
    $(window).on('resize', function () {
        if (!isMobile()) {
            $overlay.removeClass('show');
            $sidebar.removeClass('show'); // clear mobile show class
        }
    });
    // --- Bonus: Dark Mode Toggle ---
    const $themeToggleBtn = $('#theme-toggle-btn');

    $themeToggleBtn.on('click', function () {
        const $body = $('body');
        const isDark = $body.attr('data-theme') === 'dark';

        if (isDark) {
            $body.removeAttr('data-theme');
            $(this).html('<i class="fas fa-moon me-2"></i> Dark Mode');
        } else {
            $body.attr('data-theme', 'dark');
            $(this).html('<i class="fas fa-sun me-2"></i> Light Mode');
        }
    });

    // Close sidebar when clicking the dark overlay
    $overlay.on('click', function () {
        $sidebar.removeClass('show');
        $overlay.removeClass('show');
    });

    // --- Populate Mock Chat History ---
    const pastChats = [
        "AR Core Room Scanning Logic",
        "Setup RVGL dedicated server",
        "Java inner loop iterations",
        "MI Cape Town Draft Strategy",
        "Flask API local deployment"
    ];

    const $chatHistoryContainer = $('.chat-history');
    pastChats.forEach(function (title) {
        $chatHistoryContainer.append(`
            <div class="chat-history-item">
                <i class="far fa-message"></i>
                <span class="chat-history-text">${title}</span>
            </div>
        `);
    });
    // --- Mock AI Responses ---
    const aiResponses = [
        "That's a great question! I can certainly help you with that.",
        "Here is a code snippet that might solve your problem.",
        "I'm a mock AI for the CampusPe assignment, but I'm doing my best!",
        "Could you provide a bit more context so I can give a more accurate answer?",
        "As an AI language model, I don't have real feelings, but this chat UI looks fantastic!",
        "Let me think about that for a second... Okay, I have an answer for you."
    ];

    // --- Smart Keyword-Based Responses ---
    const smartResponses = [
        {
            keywords: ["who are you", "who r u", "what are you", "introduce yourself", "your name", "ur name"],
            response: "Hi there! 👋 I'm CampusPe AI, your intelligent campus assistant! I'm here to help you with coding questions, study tips, campus life queries, and much more. Think of me as your always-available academic buddy. How can I assist you today?"
        },
        {
            keywords: ["hi", "hello", "hey", "hlo", "hii", "howdy", "sup", "what's up", "whats up"],
            response: "Hello! 😊 Great to see you here. I'm CampusPe AI, ready to help. What's on your mind today?"
        },
        {
            keywords: ["how are you", "how r u", "how are u", "you doing", "ur doing"],
            response: "I'm doing great, thanks for asking! 🤖✨ As an AI, I don't have feelings, but I'm fully charged and ready to help you with anything you need. What can I do for you?"
        },
        {
            keywords: ["bye", "goodbye", "see you", "cya", "later", "good night", "goodnight"],
            response: "Goodbye! 👋 It was great chatting with you. Come back anytime you need help. Take care!"
        },
        {
            keywords: ["thank", "thanks", "thx", "ty", "appreciate"],
            response: "You're welcome! 😊 Happy to help. Feel free to ask me anything else anytime!"
        },
        {
            keywords: ["what can you do", "your features", "help me", "capabilities", "what do you do"],
            response: "I can help you with a lot of things! 🚀\n• Answer coding questions\n• Explain concepts clearly\n• Help with assignments\n• Give study tips\n• Chat about campus life\n\nJust ask away — I'm here for you!"
        }
    ];

    // --- Get AI Response (smart first, then random fallback) ---
    function getAIResponse(userMessage) {
        const lowerMsg = userMessage.toLowerCase().trim();
        for (const item of smartResponses) {
            if (item.keywords.some(keyword => lowerMsg.includes(keyword))) {
                return item.response;
            }
        }
        return aiResponses[Math.floor(Math.random() * aiResponses.length)];
    }

    // --- Part 3.2: Input Handling ---

    // Auto-resize textarea and toggle send button
    $chatInput.on('input', function () {
        // Reset height to calculate scrollHeight properly
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';

        // Enable/Disable send button based on content
        if ($(this).val().trim().length > 0) {
            $sendBtn.prop('disabled', false);
        } else {
            $sendBtn.prop('disabled', true);
        }
    });

    // Handle Enter key (Send on Enter, New line on Shift+Enter)
    $chatInput.on('keydown', function (e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault(); // Prevent default new line
            if ($(this).val().trim().length > 0) {
                sendMessage();
            }
        }
    });

    // Handle Send Button Click
    $sendBtn.on('click', function () {
        sendMessage();
    });

    // Handle Suggestion Card Clicks
    $('.suggestion-card').on('click', function () {
        const text = $(this).find('h6').text() + ' ' + $(this).find('p').text();
        $chatInput.val(text);
        $sendBtn.prop('disabled', false);
        sendMessage();
    });

    // --- Part 3.1 & 3.3: Core Logic ---

    function sendMessage() {
        const messageText = $chatInput.val().trim();
        if (!messageText) return;

        // Hide welcome screen on first message
        if ($welcomeSection.is(':visible')) {
            $welcomeSection.fadeOut(300, function () {
                $(this).remove(); // Remove from DOM completely
            });
        }

        // Add User Message
        addMessage(messageText, 'user');

        // Clear input and reset height
        $chatInput.val('');
        $chatInput.css('height', 'auto');
        $sendBtn.prop('disabled', true);

        // Simulate AI Processing
        showTypingIndicator();

        // Random delay between 1 to 2 seconds
        const delay = Math.floor(Math.random() * 1000) + 1000;

        setTimeout(function () {
            removeTypingIndicator();
            const smartReply = getAIResponse(messageText);
            addMessage(smartReply, 'assistant');
        }, delay);
    }

    function addMessage(text, sender) {
        const timeString = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        let messageHTML = '';

        if (sender === 'user') {
            messageHTML = `
                <div class="message user">
                    <div class="message-content-wrapper">
                        <div class="message-header">
                            You &bull; ${timeString}
                        </div>
                        <div class="message-bubble">${escapeHTML(text).replace(/\n/g, '<br>')}</div>
                    </div>
                    <div class="avatar">U</div>
                </div>
            `;
        } else {
            messageHTML = `
                <div class="message assistant">
                    <div class="avatar"><i class="fas fa-robot"></i></div>
                    <div class="message-content-wrapper">
                        <div class="message-header">
                            CampusPe AI &bull; ${timeString}
                        </div>
                        <div class="message-bubble">${escapeHTML(text).replace(/\n/g, '<br>')}</div>
                    </div>
                </div>
            `;
        }

        $messagesArea.append(messageHTML);
        scrollToBottom();
    }

    function showTypingIndicator() {
        const typingHTML = `
            <div class="message assistant" id="typing-indicator-msg">
                <div class="avatar"><i class="fas fa-robot"></i></div>
                <div class="message-content-wrapper justify-content-center">
                    <div class="typing-indicator">
                        <div class="typing-dot"></div>
                        <div class="typing-dot"></div>
                        <div class="typing-dot"></div>
                    </div>
                </div>
            </div>
        `;
        $messagesArea.append(typingHTML);
        scrollToBottom();
    }

    function removeTypingIndicator() {
        $('#typing-indicator-msg').remove();
    }

    function scrollToBottom() {
        $messagesArea.animate({
            scrollTop: $messagesArea.prop("scrollHeight")
        }, 300);
    }

    // Utility function to prevent XSS (Cross-Site Scripting)
    function escapeHTML(str) {
        return $('<div>').text(str).html();
    }

});