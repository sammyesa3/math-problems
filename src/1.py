import random

def generate_math_problem(difficulty):
    if difficulty == "easy":
        operands = [2, 3, 5]
        operators = ["+", "-"]
    elif difficulty == "medium":
        operands = [4, 6, 8]
        operators = ["+", "-", "*"]
    else:
        operands = [10, 12, 14]
        operators = ["+", "-", "*", "/"]
    
    problem = random.choice(operands)
    for operator in operators:
        if operator == "+":
            problem += random.choice(operands)
        elif operator == "-":
            problem -= random.choice(operands)
        elif operator == "*":
            problem *= random.choice(operands)
        else:
            problem /= random.choice(operands)
    
    return problem
