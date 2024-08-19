import random

print("This is bot.py, and I am a bot!")
print("You can end this conversation at any time by typing 'bye'.")
print("After typing each answer, press 'enter'.")
print("Let's start the conversation! How are you today?")

random_responses = ["That is quite interesting, please tell me more.",
                    "I see. Do go on.",
                    "Why do you say that?",
                    "Funny weather we've been having, isn't it?",
                    "Let's change the subject.",
                    "Did you catch the game last night?"]

while True:
    user_input = input("> ")
    if user_input.lower() == "bye":
        print("Goodbye! Have a great day!")
        break
    else:
        print(random.choice(random_responses))