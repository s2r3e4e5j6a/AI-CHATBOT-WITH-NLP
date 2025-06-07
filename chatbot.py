import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data (run this once)
try:
    nltk.data.find('corpora/wordnet')
except:
    nltk.download('wordnet')
try:
    nltk.data.find('corpora/omw-1.4')
except:
    nltk.download('omw-1.4')
try:
    nltk.data.find('tokenizers/punkt')
except:
    nltk.download('punkt')

# Define patterns and responses
# Each tuple in the 'pairs' list represents a pattern-response pair.
# The first element is a regular expression pattern that the chatbot will try to match against user input.
# The second element is a list of possible responses if the pattern matches.
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you. You can call me Bot.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you for asking!", "I'm just a program, so I don't have feelings, but I'm ready to assist you.",]
    ],
    [
        r"sorry (.*)",
        ["No worries.", "It's alright.", "No problem, please continue.",]
    ],
    [
        r"I am (.*) (good|well|ok|alright)",
        ["That's great to hear!", "Good to know!",]
    ],
    [
        r"quit|bye|exit",
        ["Goodbye! Have a great day.", "It was nice chatting with you. See you!", "Bye!"]
    ],
    [
        r"(.*) (location|city) ?",
        ["I don't have a physical location as I am a program.",]
    ],
    [
        r"how is (.*) weather ?",
        ["I'm sorry, I cannot provide real-time weather information.",]
    ],
    [
        r"what can you do ?",
        ["I can chat with you and answer basic questions based on my programming.", "I'm here to assist you with simple queries.",]
    ],
    [
        r"(.*) created you ?",
        ["I was created by a developer using Python and NLTK.",]
    ],
    [
        r"thanks|thank you",
        ["You're welcome!", "No problem!", "Glad to help!"]
    ],
    [
        r"(.*)", # Default response if no other pattern matches
        ["I'm not sure how to respond to that.", "Could you please rephrase?", "Interesting, tell me more.", "Hmm, I see."]
    ]
]

# Create a Chat instance
# The 'Chat' class takes a list of patterns and responses, and optional reflections.
# Reflections are used to transform first-person pronouns into second-person pronouns (e.g., "I am" -> "you are").
chatbot = Chat(pairs, reflections)

def start_chatbot():
    print("Hi, I'm your simple NLTK chatbot! Type 'quit' or 'bye' to exit.")
    print("How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye", "exit"]:
            print("Chatbot: Goodbye! Have a great day.")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    start_chatbot()