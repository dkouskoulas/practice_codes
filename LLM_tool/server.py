from flask import Flask, request, jsonify, send_from_directory
from API_call import ask_ollama
from flask_cors import CORS
import threading
import webbrowser
import os 

app = Flask(__name__)
CORS(app)

conversation_history = []

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

@app.route('/chat.js')
def chat_js():
    return send_from_directory('.', 'chat.js')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        global conversation_history
        data = request.get_json()
        prompt = data.get('prompt', '')

        conversation_history.append(f"User: {prompt}")

        response = ask_ollama(prompt, conversation_history)

        conversation_history.append(f"Assistant: {response}")
        
        return jsonify({'response': response})
    except Exception as e:
        print(f"Error in /chat: {e}")  # Log the error
        return jsonify({'error': str(e)}), 500

def open_browser():
    webbrowser.open_new_tab('http://localhost:5001/')

if __name__ == '__main__':
    threading.Timer(1.0, open_browser).start()
    app.run(port=5001)