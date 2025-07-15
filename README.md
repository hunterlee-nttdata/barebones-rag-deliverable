# barebones-rag-deliverable

This is a barebones implementation of a RAG (Retrieval-Augmented Generation) system, you will need to download Ollama by using the following commands:

```bash
curl -fsSL https://ollama.com/install.sh | sh

ollama serve &

ollama pull gemma3:1b
```
Every time you run the app, make sure to run the `ollama serve &` command to start the Ollama server. You will only need to do `ollama pull gemma3:1b` command once

After you have Ollama installed, you can run the following command to install the required Python packages:

```bash
pip install -r requirements.txt
```

Finally, you can run the RAG system using the following command:

```bash
python main.py
```

Your task is the following two steps:
1. Edit the prompt.py file to change the prompt used for the RAG system. Make it so that the LLM can answer questions based on the provided article summary.
2. Find an article and copy the  the article summary and question in the `main.py` file to test the RAG system with different inputs.