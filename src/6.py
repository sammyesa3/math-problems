def get_random_math_problem():
    """Return a randomly generated math problem."""
    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Determine the operation to perform based on a random number
    op = ["+", "-", "*", "/"][random.randint(0, 3)]

    # Return the problem and solution as a tuple
    return (num1, num2, op), num1 * num2
