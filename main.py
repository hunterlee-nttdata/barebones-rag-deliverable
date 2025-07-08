from prompt import PROMPT
from llm_service import ollama_chat

article_summary = """
Fill in article summary here.
"""

article_question = """
Fill in the question here.
"""

# This brings in the prompt template and fills in the placeholders with example data.
prompt = PROMPT.format(
    RESULTS=article_summary,
    QUERY=article_question
)

# Now call ollama_chat with the prompt below and print the response