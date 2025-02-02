from Chain.ChainUtils import answer_query
from VectorDB.chromaRetrieval import query_docs

def chat():
    print("RAG Chatbot: Hello! How can I assist you today?")
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit", "bye"]:
            print("RAG Chatbot: Goodbye!")
            break
        content = query_docs(query)
        response = answer_query(query, content)
        print(f"RAG Chatbot: {response}")

if __name__ == "__main__":
    chat()