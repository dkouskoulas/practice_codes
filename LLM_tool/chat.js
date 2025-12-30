window.addEventListener('DOMContentLoaded', () => {
    const chatBox = document.getElementById('chat-box');
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');

    // Add initial message
    appendMessage('ollama', "Let's get started! What is the business problem you are trying to solve?");

    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const message = userInput.value.trim();
        if (!message) return;

        appendMessage('user', message);
        userInput.value = '';

        appendMessage('ollama', '...'); // Placeholder

        try {
            const response = await fetch('http://localhost:5001/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({prompt: message})
            });
            if (!response.ok) throw new Error('Network response was not ok');
            const data = await response.json();

            // Remove placeholder and show real response
            chatBox.removeChild(chatBox.lastChild);
            appendMessage('ollama', data.response);
            chatBox.scrollTop = chatBox.scrollHeight;
        } catch (err) {
            chatBox.removeChild(chatBox.lastChild);
            appendMessage('ollama', '[Error: Could not reach server]');
        }
    });

    function appendMessage(sender, text) {
        const div = document.createElement('div');
        div.className = sender;
        div.textContent = text;
        chatBox.appendChild(div);
    }
});