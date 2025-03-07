
import random
def get_random_math_problem(level):
    """
    Generates a random math problem of the given level (easy, medium, hard)
    """
    # Create a list of operators and their corresponding levels
    operators = {
        "+": "easy",
        "-": "medium",
        "*": "hard"
    }
    # Get a random operator from the list based on the level
    op = random.choice([op for op, level in operators.items() if level == level])
    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    # Create a math problem using the operator and the two numbers
    problem = f"{num1} {op} {num2}"
    return problem