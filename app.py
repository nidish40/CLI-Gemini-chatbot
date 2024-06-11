import sys 
import os
from dotenv import load_dotenv
from chatbot1 import Chatbot

load_dotenv()

private_key = os.getenv("API_KEY")


def main():
    chatbot1 = Chatbot(api_key=private_key)
    chatbot1.start_conversation()

    print("Welcome to Nidish's Gemini Chatbot CLI. Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Exiting Chatbot. Bye...")
            sys.exit()
        try:
            response = chatbot1.send_prompt(user_input)
            print(f"{chatbot1.chatbot_name}: {response}")
        except Exception as e:
            print(f"Error: {e}")




main()