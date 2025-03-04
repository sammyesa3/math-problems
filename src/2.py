from random import randint

def get_random_math_problem():
    # Generate two random numbers
    num1 = randint(1, 10)
    num2 = randint(1, 10)

    # Generate a random operation (+, -, *, /)
    op = ['+', '-', '*', '/'][randint(0, 3)]

    # Return the problem and solution
    return f"{num1} {op} {num2} = ?", num1 {op} num2