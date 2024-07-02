import random


def generate_question():
    """Generate a basic math fact question."""
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    question = f"What is {num1} {operator} {num2}?"
    return question, answer




# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return True
        elif response == "no" or response == "n":
            return False
        else:
            print("Please enter yes / no")


# Displays instructions to user
def instructions():
    print('''

⭐⭐⭐⭐ Instructions ⭐⭐⭐⭐

There are 15 rounds and they are all basic math questions
it should be to hard.
    
!Good Luck!

    ''')


# start of code
print("Welcome to Basic Math Facts Quiz!")
if yes_no("do you want to read the instructions?      "):
    instructions()

score = 0
num_questions = 15 # You can change the number of questions here
quiz_history = []
current_question=0


while num_questions!=0:
    question, correct_answer = generate_question()
    print(f"Question {current_question + 1}: {question}")
    quiz_history.append(f"Question {current_question + 1}: {question}")

    while True:
        user_answer = input("Your answer: ")

        try:
            user_answer = int(user_answer)

            if user_answer == correct_answer:
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect. The correct answer is {correct_answer}.\n")
            quiz_history.append(f"Your answer was {user_answer}")
            quiz_history.append(f"The answer was {correct_answer}")
            quiz_history.append("")
            break

        except ValueError:
            print("Please enter a valid integer.")
    current_question=current_question+1
    num_questions=num_questions-1
if yes_no("Do you want to see the game history?"):
    print("\n⌛⌛⌛ Game History⌛⌛⌛")

    for item in quiz_history:
        print(item)


print(f"Quiz completed!\nYour score: {score}/{num_questions}")

print()
print("Thank you for playing")

