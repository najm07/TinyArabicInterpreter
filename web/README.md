# TinyInterpreter Web REPL

Web-based REPL interface for TinyInterpreter with RTL (Right-to-Left) support for Arabic text.

## Features

- **RTL Support**: Proper right-to-left display for Arabic text
- **Terminal-like Interface**: Clean, modern terminal interface
- **Interactive REPL**: Execute code line by line with full REPL functionality
- **Error Display**: Beautiful error messages with position information
- **Command History**: Navigate through previous commands with arrow keys
- **Variable Inspection**: View and manage variables
- **Unicode Normalization**: Proper handling of Arabic Unicode characters

## Setup

### Prerequisites
- Python 3.6 or higher
- Flask and flask-cors installed

### Installation

1. Install dependencies:
```bash
cd web
pip install -r requirements.txt
```

2. Run the Flask server:
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage

### Running Code
1. Type your Arabic code in the input box
2. Press Enter or click the Execute button
3. View results in the output panel

### Keyboard Shortcuts
- **Enter**: Execute code
- **Shift + Enter**: New line (for multi-line input)
- **↑/↓**: Navigate command history

### Special Commands
- `help` / `مساعدة` - Show help
- `reset` / `إعادة` - Reset interpreter
- `vars` / `متغيرات` - Show variables
- `quit` / `خروج` - Exit REPL

## Architecture

### Backend (`app.py`)
- Flask RESTful API
- Session-based interpreter state
- Error handling and normalization
- Multi-line code support

### Frontend
- **HTML** (`templates/index.html`): Main interface structure
- **CSS** (`static/css/style.css`): RTL styling and terminal theme
- **JavaScript** (`static/js/main.js`): Client-side logic and API communication

## Development

### Adding Features
1. Backend: Add new endpoints in `app.py`
2. Frontend: Update JavaScript in `main.js`
3. Styling: Modify CSS in `style.css`

### Testing
- Run the Flask server in debug mode
- Test RTL text rendering
- Verify error handling
- Test all special commands
