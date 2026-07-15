import re

conversation_history = []

knowledge_base = {
    "what is ai": "Artificial Intelligence (AI) is the simulation of human intelligence in machines.",
    "what is machine learning": "Machine Learning is a branch of AI that enables computers to learn from data.",
    "what is python": "Python is a high-level programming language widely used in AI, Machine Learning, and Web Development.",
    "what is chatbot": "A chatbot is a software application designed to simulate human conversation.",
    "what is deep learning": "Deep Learning is a subset of Machine Learning that uses neural networks with multiple layers.",
    "what is data science": "Data Science is the process of extracting useful insights from data using statistics, programming, and machine learning."
}

def log_conversation(user_message, bot_message):
    conversation_history.append(("User", user_message))
    conversation_history.append(("Bot", bot_message))

def print_history():
    print("\n========== Conversation History ==========\n")

    for speaker, message in conversation_history:
        print(f"{speaker}: {message}")

    print("\n==========================================\n")

def chatbot_response(user_input):
    message = user_input.lower().strip()

    if re.search(r"\b(hi|hello|hey|good morning|good evening)\b", message):
        return "Hello! How can I help you today?"

    elif "help" in message:
        return (
            "I can help you with:\n"
            "- Greetings\n"
            "- Small Talk\n"
            "- AI related questions\n"
            "- Type 'history' to view conversation history\n"
            "- Type 'exit' to end the chat"
        )

    elif "how are you" in message:
        return "I'm doing great! Thanks for asking."

    elif "your name" in message:
        return "I'm a Simple Rule-Based Chatbot."

    elif "who created you" in message:
        return "I was created using Python with pattern matching rules."

    elif "thank you" in message or "thanks" in message:
        return "You're welcome!"

    elif "bye" in message or "goodbye" in message:
        return "Goodbye! Have a wonderful day!"

    elif message in knowledge_base:
        return knowledge_base[message]

    else:
        return (
            "Sorry, I don't understand that.\n"
            "Type 'help' to see what I can do."
        )

def main():
    print("=" * 50)
    print("       SIMPLE RULE-BASED CHATBOT")
    print("=" * 50)

    print("\nType 'help' to see available commands.")
    print("Type 'history' to view conversation history.")
    print("Type 'exit' to quit.\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            bot_reply = "Goodbye! Thank you for chatting."
            print(f"Bot: {bot_reply}")
            log_conversation(user_input, bot_reply)
            break

        if user_input.lower() == "history":
            print_history()
            continue

        bot_reply = chatbot_response(user_input)

        print(f"Bot: {bot_reply}")

        log_conversation(user_input, bot_reply)

    print("\nFinal Conversation Log:")
    print_history()

if __name__ == "__main__":
    main()