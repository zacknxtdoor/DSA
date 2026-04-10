def power_digit_sum(n: int) -> int:
    """
    Problem 16
    Takes an integer n as input and returns 
    sum of digits in the integer 2 raised to n
    """
    digits = []
    dig_str = str(2 ** n)
    for i in range(len(dig_str)):
        digits.append(int(dig_str[i]))
    return sum(digits)

print(power_digit_sum(1000))