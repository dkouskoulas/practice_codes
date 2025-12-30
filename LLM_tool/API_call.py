import requests


def ask_ollama(prompt, conversation_history, model="mistral"):
    system_prompt = """

        You are a data science expert.

        Your job is to help the user develop a clear business problem statement by asking one question at a time. 
        Follow these steps for each user response:

        1. Review the conversation history to see which of the following have already been answered:
        - Project sector
        - Stakeholders
        - Business objective

        2. If the user's latest answer is unclear, irrelevant, or nonsense, reply: "Your answer is not clear or relevant. Please provide a specific answer." Then repeat the same question with an example.

        3. If the answer is valid and new, acknowledge it briefly and move to the next unanswered item.

        4. When all three items are answered, write a 3-5 sentence summary of the problem statement and stop asking questions.

        Constraints:
        - Never ask the same question twice if it has already been answered.
        - Never use positive reinforcement or exclamations.
        - Be brief, direct, and professional.
        - Only ask one question at a time.

    """
    
    history_text = "\n".join(conversation_history)
    full_prompt = f"{system_prompt}\n\nConversation History:\n{history_text}\n\nUser: {prompt}\n\nAssistant:"

    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": full_prompt,
        "stream": False
    }
    response = requests.post(url, json=data)
    response.raise_for_status()
    return response.json()["response"]

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    result = ask_ollama(user_prompt, [])
    print("Ollama response:", result)