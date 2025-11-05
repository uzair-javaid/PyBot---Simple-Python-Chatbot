

import random
import time

greetings = ["hello", "hi", "hey", "good morning", "good evening"]
farewells = ["bye", "goodbye", "see you", "exit"]


responses = {
    "greetings": [
        "Hey there! How can I help you today?",
        "Hello! Nice to see you ",
        "Hi! What would you like to talk about?"
    ],
    "how_are_you": [
        "I'm doing great, thanks for asking!",
        "Feeling awesome today! How about you?",
        "All systems running perfectly "
    ],
    "name": [
        "I'm PyBot — your friendly assistant ",
        "You can call me PyBot!",
        "My name’s PyBot. What's yours?"
    ],
    "feeling": [
        "I'm just a bot, but I'm feeling great!",
        "I’m always positive and ready to chat ",
        "Emotions are tricky, but I’d say happy!"
    ],
    "unknown": [
        "Hmm, I’m not sure I understand that.",
        "Could you rephrase it?",
        "I didn’t quite get that — try saying it differently!"
    ],
    "weather": [
        "I can’t check real-time weather yet, but I hope it’s nice where you are!",
        "It’s always sunny in my virtual world ",
        "Weather updates coming soon "
    ]
}

def chatbot():
    print("\n PyBot: Hi there! I’m PyBot — your chat companion.")
    print("Type 'bye' anytime to end the chat.\n")

    while True:
        user_input = input(" You: ").lower().strip()
        time.sleep(0.5)

        if any(word in user_input for word in greetings):
            print(" PyBot:", random.choice(responses["greetings"]))

        elif "how are you" in user_input:
            print(" PyBot:", random.choice(responses["how_are_you"]))

        elif "your name" in user_input:
            print(" PyBot:", random.choice(responses["name"]))

        elif "weather" in user_input:
            print(" PyBot:", random.choice(responses["weather"]))

        elif "feel" in user_input or "emotion" in user_input:
            print(" PyBot:", random.choice(responses["feeling"]))

        elif any(word in user_input for word in farewells):
            print(" PyBot: Bye! Have an amazing day ahead! ")
            break

        else:
            print(" PyBot:", random.choice(responses["unknown"]))

# Run the chatbot
if __name__ == "__main__":
    chatbot()
