import random

def generate_random_numbers(quantity, start, end):
    """
    Generate a list of random numbers.

    Parameters:
    quantity (int): The number of random numbers to generate.
    start (int): The lower bound of the range of numbers.
    end (int): The upper bound of the range of numbers.

    Returns:
    list: A list of random numbers.
    """
    return [random.randint(start, end) for _ in range(quantity)]
