def multiples_of_3_or_5(n : int) -> int:
    """
    Problem 1
    Takes an integer n as input and finds the sum of all 
    multiples of 3 or 5 below n
    """
    multiples = []
    for i in range(n):
        if (i % 3 == 0) or (i % 5 == 0):
            multiples.append(i)
    return sum(multiples)


print(multiples_of_3_or_5(1000))
    

