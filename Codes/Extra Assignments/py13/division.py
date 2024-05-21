def division(a, b):
    try:
        div = a / b
    except ZeroDivisionError:
        return "can't divide by 0!"
    except TypeError:
        return "unsupported operand type(s) for division"
    return f"{a}/{b} = {div}"