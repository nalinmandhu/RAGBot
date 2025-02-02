from langchain_google_genai import ChatGoogleGenerativeAI
import os
import json
from dotenv import load_dotenv

load_dotenv()

GEMINI_MODEL = os.environ.get("LLM")
API_KEY = os.environ.get("API_KEY")
CHAT_HISTORY_FILE = "chat_history.json"
MAX_HISTORY_LENGTH = 3

#Currently saving chat history in local. We can also save the history in a database and call it each time
def save_chat_history(query, response):
    """Saves the chat history, keeping only the last MAX_HISTORY_LENGTH entries."""
    try:
        if os.path.exists(CHAT_HISTORY_FILE):
            with open(CHAT_HISTORY_FILE, "r") as f:
                chat_history = json.load(f)
        else:
            chat_history = []

        chat_history.append({"query": query, "response": response})

        # Keep only the last MAX_HISTORY_LENGTH entries
        if len(chat_history) > MAX_HISTORY_LENGTH:
            chat_history = chat_history[-MAX_HISTORY_LENGTH:]  # Slice to keep last N

        with open(CHAT_HISTORY_FILE, "w") as f:
            json.dump(chat_history, f, indent=4)  # indent for readability

    except Exception as e:
        print(f"Error saving chat history: {e}")


def load_chat_history():
    """Loads and returns the chat history. Returns an empty list if no history exists."""
    try:
        if os.path.exists(CHAT_HISTORY_FILE):
            with open(CHAT_HISTORY_FILE, "r") as f:
                return json.load(f)
        else:
            return []  # Return empty list if file doesn't exist
    except Exception as e:
        print(f"Error loading chat history: {e}")
        return []

def answer_query(query, content):
    

    llm_model = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL,
    api_key=API_KEY,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    )
    chat_history = load_chat_history()
    messages = [
    (
        "system",
        f'''## You are a helpful assistant that answers queries related to Ubuntu using reference information, chat history and the given instructions.
        # Reference Information : {content}
        # Chat History: {chat_history}

        ## Instructions to follow:
        # 1. Answer queries involving multiple tasks in steps. Each step should be on different lines.
        # 2. Answer only using the reference information.

        # Return only the required answer.''',
    ),
    ("human", query),
    ]
    ai_msg = llm_model.invoke(messages).content
    save_chat_history(query, ai_msg)
    return ai_msg
