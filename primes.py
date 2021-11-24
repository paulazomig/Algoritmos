import math

# PRIME NUMBERS - LINEAR
def prime_linear(input_value):
    try:
        n = int(input_value)
        if n < 2:
            return None
    except ValueError:
        return None

    prime_numbers = [2]

    for i in range(3, (n + 1), 2):
        divisors = 0
        for j in range(2, round(math.sqrt(i)) + 1):
            if i % j == 0:
                divisors += 1
        if divisors == 0:
            prime_numbers.append(i)

    return prime_numbers


# PRIME NUMBERS - RECURSIVE
def prime_recursive (input_value):
    try:
        n = int(input_value)
        if n < 2:
            return None
    except ValueError:
        return None
    return _prime_recursive(input_value)


def _prime_recursive(n, prime_check = 3, prime_numbers = [2]):
    divisors = 0

    for j in range(2, round(math.sqrt(prime_check))+1):
        if prime_check % j == 0:
            divisors += 1
    if divisors == 0:
        prime_numbers.append(prime_check)
    
    if prime_check == n:
        return prime_numbers
   
    prime_check += 2
    if prime_check > n:
        return prime_check
    return _prime_recursive(n, prime_check, prime_numbers)
