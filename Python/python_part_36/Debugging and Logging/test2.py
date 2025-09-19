def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return None