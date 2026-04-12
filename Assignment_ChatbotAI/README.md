# CampusPe Gen AI Assignment - Chat UI

## Description
This project is a modern, responsive chat user interface built as part of the CampusPe Gen AI Assignment. It mimics the look and feel of popular AI chatbots like ChatGPT and Claude. The interface is built entirely on the frontend using HTML, CSS, JavaScript, jQuery, and Bootstrap 5, requiring no backend.

## Features
* **Semantic UI Structure:** Clean, accessible HTML5 layout.
* **Responsive Layout:** Fully mobile-responsive design with an off-canvas sidebar for smaller screens, powered by Bootstrap 5 and custom CSS.
* **Interactive Input Area:** Auto-resizing textarea that enables the send button only when text is present. Supports 'Enter' to send and 'Shift+Enter' for new lines.
* **Simulated AI Interaction:** Simulates network delay with an animated typing indicator (bouncing dots) before responding with mock AI text.
* **Dynamic Chat History:** Sidebar features a scrollable chat history (mocked data).
* **Smooth Animations:** Hover effects on buttons/cards and fade-in animations for new messages.

## Bonus Features Implemented
* **Dark Mode Toggle:** Smooth theme transition between Light and Dark mode using CSS custom properties.
* **Text Formatting:** Supports basic markdown parsing in the chat interface:
    * Bold (`**text**`)
    * Italic (`*text*`)
    * Code blocks (```` ```code``` ````)

## How to Run
1.  Extract the ZIP folder.
2.  Navigate into the extracted folder.
3.  Open the `index.html` file in any modern web browser (Google Chrome, Firefox, Edge, Safari).
4.  No build tools, local servers, or npm installations are required.

## File Structure
```
YourName_ChatUI/
├── index.html        # Main HTML file containing the app structure
├── css/
│   └── style.css     # Custom CSS styling and variables
├── js/
│   └── chat.js       # JavaScript and jQuery logic
├── screenshots/      # UI screenshots on desktop, tablet, and mobile
└── README.md         # Project documentation
```

## Technologies Used
* HTML5
* CSS3 (Custom Properties, Flexbox, Animations)
* JavaScript (ES6+)
* jQuery 3.7.1
* Bootstrap 5.3.2
* Font Awesome 6.4.2
* Google Fonts (Inter)
