from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
import nltk
nltk.download('punkt_tab')
# import and create a Conll extractor to use later 
extractor = ConllExtractor()

def main():
    print("This is bot.py, and I am a bot!")
    print("You can end this conversation at any time by typing 'bye'.")
    print("After typing each answer, press 'enter'.")
    print("Let's start the conversation! How are you today?")

    while True:
        user_input = input("> ")
        if user_input.lower() == "bye":
            print("Goodbye! Have a great day!")
            break
        else:
            user_input_blob = TextBlob(user_input, np_extractor=extractor)  # note non-default extractor specified
            np = user_input_blob.noun_phrases
            response = ""
            if user_input_blob.polarity <= -0.5:
                response = "Oh dear, that sounds bad. "
            elif user_input_blob.polarity <= 0:
                response = "Hmm, that's not great. "
            elif user_input_blob.polarity <= 0.5:
                response = "Well, that sounds positive. "
            elif user_input_blob.polarity <= 1:
                response = "Wow, that sounds great. "

            if len(np) != 0:
                # There was at least one noun phrase detected, so ask about that and pluralise it
                # e.g. cat -> cats or mouse -> mice
                response = response + "Can you tell me more about " + np[0].pluralize() + "?"
            else:
                response = response + "Can you tell me more?"
            print(response)

main()