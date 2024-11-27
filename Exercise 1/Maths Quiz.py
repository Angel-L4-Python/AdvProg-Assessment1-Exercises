import random

def displayMenu():
    print("DIFFICULTY LEVEL")
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")

def randomInt(difficulty):
    # Easy
    if difficulty == 1:
        return random.randint(0, 9), random.randint(0, 9)
    # Moderate
    elif difficulty == 2:
        return random.randint(10, 99), random.randint(10, 99)
    # Advanced
    elif difficulty == 3:
        return random.randint(1000, 9999), random.randint(1000, 9999)

def decideOperation():
    return random.choice(['+', '-'])

def displayProblem(num1, num2, operation):
    return num1 + num2 if operation == '+' else num1 - num2

def isCorrect(user_answer, correct_answer):
    return user_answer == correct_answer

def displayResults(score):
    print(f"Your final score is {score} out of 100.")
    if score >= 90:
        print("Grade: A+")
        print("Excellent work! You're a math whiz!\n")
    elif score >= 80:
        print("Grade: A")
        print("Great job! Keep practicing!\n")
    elif score >= 70:
        print("Grade: B")
        print("Good effort! You can improve even more!\n")
    elif score >= 60:
        print("Grade: C")
        print("Not bad, but there's room for improvement!\n")
    elif score >= 50:
        print("Grade: D")
        print("Keep practicing, and you'll get better!\n")
    else:
        print("Grade: F")
        print("Don't be discouraged! Every mistake is a learning opportunity.\n")

def playQuiz():
    score = 0

    while True:
        try:
            difficulty = int(input("Select difficulty level (1-3): "))
            if difficulty in [1, 2, 3]:
                break
            else:
                print("Invalid input. Please select a difficulty level (1-3).")
        except ValueError:
            print("Invalid input. Please enter a number (1-3).")
    
    for _ in range(10):
        num1, num2 = randomInt(difficulty)
        operation = decideOperation()
        correct_answer = displayProblem(num1, num2, operation)
        
        for attempt in range(2):
            try:
                user_answer = int(input(f"{num1} {operation} {num2} = "))
                if isCorrect(user_answer, correct_answer):
                    print("Correct!")
                    score += 10 if attempt == 0 else 5
                    break
                else:
                    print("Incorrect. Try again." if attempt == 0 else "Still incorrect.")
            except ValueError:
                print("Please enter a valid number.")

    displayResults(score)

def main():
    print("Welcome to Math Quiz!")
    print("Choose your difficulty level and earn points based on your answers.\n")
    
    while True:
        displayMenu()
        playQuiz()
        
        while True:
            play_again = input("Would you like to play again? (yes/no): ").strip().lower()
            if play_again == 'yes':
                print("\n")
                break
            elif play_again == 'no':
                print("Thank you for playing! Goodbye!")
                return
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()