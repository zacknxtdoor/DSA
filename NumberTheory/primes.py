import math

def sieve(n):
    """Implementation of the Sieve of Eratosthenes 
    which takes an integer n > 1 as input and returns 
    all primes less than n
    """
    if n < 2: # smallest prime integer is 2
        return []
    
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False # Want to start from indices 2 up to n

    for p in range(2, n + 1):
        if primes[p]:
            for j in range(p * p, n, p): # iterating through the multiples of a given prime p
                primes[j] = False

    return [i for i in range(len(primes)) if primes[i] == True]


    

def euler_totient(n):
    """Implementation of the mathematical function 
    which akes an integer n  > 1 as input and 
    returns all integers less than and relatively
    prime to n
    """
    coprimes = []
    for i in range(n):
        if math.gcd(i, n) == 1:
            coprimes.append(i)
    return coprimes

if __name__ == "__main__":
    print(sieve(10)) # [2, 3, 5, 7, 9]
    print(euler_totient(7)) #1, 2, 3, 4, 5, 6