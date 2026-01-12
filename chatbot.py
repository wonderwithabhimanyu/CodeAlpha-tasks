def chatbot_codealpha(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


def run_chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = chatbot_codealpha(user_input)
        print("Chatbot:", response)

        if user_input.lower() == "bye":
            break


# Run this alpha bot
run_chatbot()