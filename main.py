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


def main():
    print("Welcome to Basic Math Facts Quiz!")
    score = 0
    num_questions = 5  # You can change the number of questions here

    for _ in range(num_questions):
        question, correct_answer = generate_question()
        print(question)
        user_answer = input("Your answer: ")

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.\n")

    print(f"Quiz completed!\nYour score: {score}/{num_questions}")


if __name__ == "__main__":
    main()
