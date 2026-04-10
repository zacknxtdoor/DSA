

def even_fib(n : int) -> int:
    """
    Problem 2
    Takes an integer n as input and finds the sum of the even-valued terms
    in the Fibonacci sequence whose values do not exceed n
    """
    lst = []
    i = 0 
    ith_fib_num = i # Keeps track of the ith Fibonacci number
    lst.append(ith_fib_num)
    while ith_fib_num <= n:
        ith_fib_num = fib(i)
        if ith_fib_num % 2 == 0:
            lst.append(ith_fib_num)
        i += 1
    return sum(lst)

def fib(n: int) -> int: 
    # helper function that finds the nth fibonacci number 
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
    
print(even_fib(4000000))
