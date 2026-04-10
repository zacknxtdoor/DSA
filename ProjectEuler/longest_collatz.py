def longest_collatz(n: int) -> str:
    """
    Problem 14
    Takes an integer n as input and returns the starting number less than n that 
    generates the longest Collatz chain 
    """
    max_chain = []
    starting_num = 1
    for i in range(2, n):
        chain = collatz(i)
        if len(chain) > len(max_chain):
            max_chain = chain
            starting_num = i
    return f"The longest Collatz chain up to {n} starts with {starting_num} with length {len(max_chain)}"


def collatz(n): # Helper function which uses the Collatz Sequence
    chain = []
    chain.append(n)
    while n > 1:
        if n % 2 == 0:
            n /= 2
            chain.append(int(n))
        else:
            n = (3 * n) + 1
            chain.append(int(n))
    return chain

print(longest_collatz(1000000))