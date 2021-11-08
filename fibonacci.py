# FIBONACCI - LINEAR
def fibonacci_linear(input_value):
    try:
        n = int(input_value)
        if n < 0:
            return None
    except ValueError:
        return None

    fibonacci = (0, 1)

    if n < 2:
        return fibonacci[n]
    else:
        for i in range (n-1):
            new_value = fibonacci[0] + fibonacci[1]
            fibonacci = (fibonacci[1], new_value)
        return fibonacci[1]


# FIBONACCI - RECURSIVE
def fibonacci_recursive(input_value):
    try:
        n = int(input_value)
        if n < 0:
            return None
    except ValueError:
        return None
    return _fibonacci_recursive(input_value)


def _fibonacci_recursive(n, counter = 2, fibonacci = (0,1)):
    new_value = fibonacci[0] + fibonacci[1]
    new_fibonacci = (fibonacci[1], new_value)

    if n == (counter):
        return new_fibonacci[1]
    
    counter += 1
    return _fibonacci_recursive(n, counter, new_fibonacci)
