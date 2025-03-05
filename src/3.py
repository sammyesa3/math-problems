import random

def get_random_math_problem(max_value=100):
    operator = random.choice(['+', '-', '*', '/'])
    problem = f"{random.randint(1, max_value)} {operator} {random.randint(1, max_value)}"
    return problem
