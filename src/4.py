import random

def get_random_math_problem(min_value=0, max_value=100):
    """
    Generates a random math problem with two operands and one operator.
    :param min_value: The minimum value of the operands
    :param max_value: The maximum value of the operands
    :return: A string representing the math problem
    """
    op1 = random.randint(min_value, max_value)
    op2 = random.randint(min_value, max_value)
    operator = ['+', '-', '*', '/'][random.randint(0, 3)]
    problem = f'{op1} {operator} {op2}'
    return problem