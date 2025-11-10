def chatbot():
    print(" Chatbot: Hello! I’m your friendly chatbot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi", "hey"]:
            print(" Chatbot: Hi there! How can I help you today?")
        
        elif user_input in ["how are you", "how are you doing"]:
            print(" Chatbot: I'm doing great, thanks for asking! How about you?")
        
        elif user_input in ["i am fine", "i’m good", "good", "fine"]:
            print(" Chatbot: That’s awesome to hear! ")
        
        elif user_input in ["what is your name", "who are you"]:
            print(" Chatbot: I’m your simple chatbot created in Python.")
        
        elif user_input in ["what can you do", "help", "commands"]:
            print(" Chatbot: I can chat with you! Try saying hello, asking how I am, or say bye to end the chat.")
        
        elif user_input in ["thank you", "thanks"]:
            print(" Chatbot: You’re welcome! ")
        
        elif user_input in ["bye", "exit", "quit"]:
            print(" Chatbot: Goodbye! Have a great day! ")
            break
        
        else:
            print(" Chatbot: Hmm... I didn’t quite get that. Could you say it differently?")

# Run the chatbot
chatbot()
