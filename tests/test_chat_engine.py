from rag.chat_engine import ChatEngine

if __name__ == "__main__":

    chat = ChatEngine()

    question = input("Ask a question: ")

    answer = chat.ask(question)

    print("\n" + "=" * 60)
    print("Answer")
    print("=" * 60)
    print(answer)
