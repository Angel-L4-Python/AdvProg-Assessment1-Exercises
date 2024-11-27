import random

def load_jokes(file_path):
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        jokes = [line.strip() for line in file if line.strip()]
    return jokes

def tell_joke(joke):
    setup, punchline = joke.split('?', 1)
    print(f"Alexa: {setup}?")
    input("Press Enter to keep things rolling!")
    print(f"Alexa: {punchline.strip()}")

def main():
    jokes = load_jokes('resources/randomJokes.txt')
    print("'Alexa tell me a joke' to start")
    
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "alexa tell me a joke":
            joke = random.choice(jokes)
            tell_joke(joke)
        elif user_input == "quit":
            print("Time to leaf!")
            break
        else:
            print("Please say 'Alexa tell me a joke' or 'quit' to exit.")

if __name__ == "__main__":
    main()