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
    // --- Backend API Configuration ---
    const API_URL = 'http://localhost:5000/api/chat';

    // --- Conversation History ---
    let messages = [];

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

    async function sendMessage() {
        const messageText = $chatInput.val().trim();
        if (!messageText) return;

        // Hide welcome screen on first message
        if ($welcomeSection.is(':visible')) {
            $welcomeSection.fadeOut(300, function () {
                $(this).remove(); // Remove from DOM completely
            });
        }

        // Add user message to conversation history
        messages.push({ role: 'user', content: messageText });

        // Add User Message to UI
        addMessage(messageText, 'user');

        // Clear input and reset height
        $chatInput.val('');
        $chatInput.css('height', 'auto');
        $sendBtn.prop('disabled', true);

        // Show typing indicator while waiting for backend
        showTypingIndicator();

        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ messages: messages }),
            });

            const data = await response.json();
            removeTypingIndicator();

            if (!response.ok || data.error) {
                addMessage('⚠️ ' + (data.error || 'Something went wrong. Please try again.'), 'assistant');
                return;
            }

            // Add assistant reply to conversation history
            messages.push({ role: 'assistant', content: data.reply });

            addMessage(data.reply, 'assistant');
        } catch (err) {
            removeTypingIndicator();
            addMessage('⚠️ Could not reach the server. Make sure the Flask backend is running on http://localhost:5000.', 'assistant');
        }
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
            // Custom Markdown renderer for code blocks (Marked v12+ API)
            const renderer = {
                code(token) {
                    const codeContent = typeof token === 'string' ? token : token.text;
                    const lang = typeof token === 'string' ? arguments[1] : token.lang;
                    const langMatch = (lang || 'plaintext').toLowerCase();

                    return `
                        <div class="code-block-wrapper">
                            <div class="code-block-header">
                                <span class="code-block-lang">${langMatch}</span>
                                <button class="copy-btn" onclick="navigator.clipboard.writeText(this.parentElement.nextElementSibling.innerText)">Copy</button>
                            </div>
                            <pre><code class="language-${langMatch}">${codeContent}</code></pre>
                        </div>
                    `;
                }
            };
            marked.use({ renderer });

            // Parse Markdown for assistant responses
            const rendered = marked.parse(text);
            messageHTML = `
                <div class="message assistant">
                    <div class="avatar"><i class="fas fa-robot"></i></div>
                    <div class="message-content-wrapper">
                        <div class="message-header">
                            CampusPe AI &bull; ${timeString}
                        </div>
                        <div class="message-bubble markdown-body"><div class="ai-markdown-content">${rendered}</div></div>
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

    // --- Voice-to-Text (Web Speech API) ---
    const micBtn = document.getElementById('mic-btn');

    if ('SpeechRecognition' in window || 'webkitSpeechRecognition' in window) {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        const recognition = new SpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = 'en-US';

        recognition.onstart = function () {
            micBtn.classList.add('listening');
        };

        recognition.onresult = function (event) {
            const transcript = event.results[0][0].transcript;
            // Append transcript to the textarea
            const input = document.getElementById('chat-input');
            input.value += transcript;
            // Fire 'input' event so the send-button enable logic triggers
            input.dispatchEvent(new Event('input', { bubbles: true }));
        };

        recognition.onerror = function (event) {
            console.error('Speech recognition error:', event.error);
            micBtn.classList.remove('listening');
        };

        recognition.onend = function () {
            micBtn.classList.remove('listening');
        };

        micBtn.addEventListener('click', () => {
            micBtn.classList.contains('listening') ? recognition.stop() : recognition.start();
        });
    } else {
        micBtn.style.display = 'none';
        console.warn('Web Speech API is not supported in this browser.');
    }

});