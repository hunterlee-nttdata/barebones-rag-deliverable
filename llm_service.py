import ollama

# Function to interact with the Ollama API using the Gemma 3 model
def ollama_chat(prompt):
    response = ollama.chat(
        model='gemma3:1b',
        messages=[{'role': 'user', 'content': prompt}]
    )

    return response