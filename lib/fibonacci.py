"""
The fibonacci module
"""

def fibonacci(length):
    """
    Return a specified length of Fibonacci sequence, a recursive implementation

    Arguments:
    length - Specify the length of the Fibonacci sequence to be returned

    Returns:
    The list of Fibonacci sequence

    Raises:
    Exception - A negative length is specified
    """
    if length < 0:
        raise Exception("The input length %d is invalid" % length)
    elif length == 0:
        return []
    elif length == 1:
        return [0]
    elif length == 2:
        return [0, 1]
    else:
        result = fibonacci(length - 1)
        result.append(result[-2] + result[-1])
        return result

def fibonacci_non_recursive(length, base=None):
    """
    Return a specified length of Fibonacci sequence
    A non-recursive implementation of fibonacci

    Arguments:
    length - Specify the length of the Fibonacci sequence to be returned
    base - Specify an existing fibonacci sequence so this function will do operation/calculation based on it

    Returns:
    The list of Fibonacci sequence

    Raises:
    Exception - A negative length is specified
    """
    if length < 0:
        raise Exception("The input length %d is invalid" % length)

    # There is no base input, calculate from scratch
    if base is None:
        result = []
        index = 0
    else:
        # The input length is less than the base, fetch from base directly
        if length < len(base):
            return base[:length]
        # The input length is greater than the base, do further calculation based on it
        else:
            result = list(base)
            index = len(result) + 1
        
    while index <= length:
        if index == 0:
            pass
        elif index == 1:
            result.append(0)
        elif index == 2:
            result.append(1)
        else:
            result.append(result[-2] + result[-1])
        index += 1
    return result
        
