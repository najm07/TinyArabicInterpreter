// JavaScript for TinyInterpreter Web REPL

let commandHistory = [];
let historyIndex = -1;

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    const input = document.getElementById('input');
    
    // Auto-resize textarea
    input.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
    });
    
    // Handle Enter key
    input.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            executeCode();
        } else if (e.key === 'ArrowUp') {
            e.preventDefault();
            navigateHistory(-1);
        } else if (e.key === 'ArrowDown') {
            e.preventDefault();
            navigateHistory(1);
        }
    });
});

function executeCode() {
    const input = document.getElementById('input');
    const code = input.value.trim();
    
    if (!code) {
        return;
    }
    
    // Handle special commands
    if (code.toLowerCase() === 'help' || code === 'مساعدة') {
        showHelp();
        input.value = '';
        addToHistory(code);
        return;
    }
    
    if (code.toLowerCase() === 'quit' || code === 'خروج') {
        addOutputLine('👋 وداعاً! Goodbye!', 'info');
        addToHistory(code);
        input.value = '';
        return;
    }
    
    // Display the command
    addCommandLine(code);
    
    // Add to history
    addToHistory(code);
    
    // Clear input
    input.value = '';
    input.style.height = 'auto';
    
    // Execute via API
    fetch('/execute', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ code: code })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            if (data.output) {
                addOutputLine(data.output, 'success');
            }
        } else {
            // Handle error
            if (data.error) {
                let errorMsg = `❌ ${data.error.type}: ${data.error.message}`;
                if (data.error.position) {
                    errorMsg += `\n📍 Location: line ${data.error.position.line}, column ${data.error.position.column}`;
                }
                addOutputLine(errorMsg, 'error');
            }
        }
    })
    .catch(error => {
        addOutputLine(`❌ Network error: ${error.message}`, 'error');
    });
}

function resetInterpreter() {
    fetch('/execute', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ code: 'reset' })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            addOutputLine(data.output, 'info');
        }
    });
}

function showVariables() {
    fetch('/execute', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ code: 'vars' })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            addOutputLine(data.output, 'success');
        }
    });
}

function clearOutput() {
    const output = document.getElementById('output');
    output.innerHTML = '<div class="welcome-message"><h2>🎉 مرحبا بك في مترجم اللغة العربية</h2><p>🎉 Welcome to the Arabic Language Interpreter REPL</p><hr><p>📝 Type Arabic code and press Enter to execute</p><p>📝 Type \'help\' or \'مساعدة\' for commands, \'quit\' or \'خروج\' to exit</p><p>📝 Use square brackets [] for compound statements</p></div>';
}

function showHelp() {
    const helpText = `📚 Available Commands / الأوامر المتاحة:
  help / مساعدة     - Show this help message
  quit / خروج       - Exit the REPL
  reset / إعادة     - Reset interpreter state
  vars / متغيرات    - Show all variables

📝 Language Syntax / صيغة اللغة:
  اكتب expression     - Print expression
  variable = value     - Assign variable
  اذا condition statement - If statement
  بينما condition [ statements ] - While loop
  لكل var في start حتى end [ statements ] - For loop

📝 Examples / أمثلة:
  x = 10
  اكتب x + 5
  اذا x > 5 اكتب 'كبير'`;
    
    addOutputLine(helpText, 'info');
}

function addCommandLine(code) {
    const output = document.getElementById('output');
    const line = document.createElement('div');
    line.className = 'output-line';
    line.innerHTML = `<span class="prompt-arrow">>>></span> <span class="code-text">${escapeHtml(code)}</span>`;
    output.appendChild(line);
    output.scrollTop = output.scrollHeight;
}

function addOutputLine(text, type = 'success') {
    const output = document.getElementById('output');
    const line = document.createElement('div');
    line.className = `output-line ${type}`;
    
    // Preserve line breaks and handle RTL/LTR
    const lines = text.split('\n');
    let html = '';
    for (let txt of lines) {
        html += `<div class="${isArabic(txt) ? 'arabic-text' : 'code-text'}">${escapeHtml(txt)}</div>`;
    }
    
    line.innerHTML = html;
    output.appendChild(line);
    output.scrollTop = output.scrollHeight;
}

function addToHistory(command) {
    // Remove from history if it exists
    const index = commandHistory.indexOf(command);
    if (index > -1) {
        commandHistory.splice(index, 1);
    }
    
    // Add to beginning
    commandHistory.unshift(command);
    
    // Keep only last 50 commands
    if (commandHistory.length > 50) {
        commandHistory = commandHistory.slice(0, 50);
    }
    
    historyIndex = -1;
}

function navigateHistory(direction) {
    if (commandHistory.length === 0) {
        return;
    }
    
    historyIndex += direction;
    
    if (historyIndex < 0) {
        historyIndex = -1;
        document.getElementById('input').value = '';
        return;
    }
    
    if (historyIndex >= commandHistory.length) {
        historyIndex = commandHistory.length - 1;
    }
    
    document.getElementById('input').value = commandHistory[historyIndex];
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function isArabic(text) {
    // Check if text contains Arabic characters
    const arabicRegex = /[\u0600-\u06FF]/;
    return arabicRegex.test(text);
}
