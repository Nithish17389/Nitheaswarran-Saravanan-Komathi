import random

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer within a specified range.
    
    Parameters:
        min_value (int): The minimum integer value.
        max_value (int): The maximum integer value.
    
    Returns:
        int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def choose_operator():
    """
    Randomly select an arithmetic operator from a predefined list.
    
    Returns:
        str: A random operator ('+', '-', or '*').
    """
    return random.choice(['+', '-', '*'])

def create_problem_and_answer(num1, num2, operator):
    """
    Create a math problem string and compute its answer based on given operands and operator.
    
    Parameters:
        num1 (int): The first number in the problem.
        num2 (int): The second number in the problem.
        operator (str): The operator to use ('+', '-', '*').
    
    Returns:
        tuple: A tuple containing the problem as a string and the answer as an integer.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem, answer

def math_quiz():
    """
    Conduct a math quiz game with the user, presenting math problems and checking user answers.
    
    Returns:
        None
    """
    score = 0
    total_questions = 3  # Number of questions to ask

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate random numbers and an operator for the math problem
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 10)
        operator = choose_operator()

        # Generate the math problem and its correct answer
        problem, correct_answer = create_problem_and_answer(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")
        except ValueError:
            print("Invalid input! Please enter an integer.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
