def sum_square_diff(n: int) -> int:
    """
    Problem 6
    Takes an integer n as input and returns the difference
    between the sum of the squares of the first n natural numbers
    and the square of the sum
    """
    # the sum of the squares of the first n natural numbers
    squares_sum = sum([i * i for i in range(1, n + 1)]) 
    # the square of the sum of the first n natural numbers
    sum_squared = sum([i for i in range(1, n + 1)]) ** 2
    return sum_squared - squares_sum


