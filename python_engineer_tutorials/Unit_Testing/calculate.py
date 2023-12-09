def add(x, y):
    """ add two values."""
    return x + y

def substract(x, y):
    """subtract two values."""
    return x - y

def multiply(x, y):
    """ multiply two values."""
    return x * y

def divide(x, y):
    """ divide two values."""
    if y == 0:
        raise ValueError('Can not divide by zero !!')
    return x / y