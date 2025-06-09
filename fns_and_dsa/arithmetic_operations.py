def perform_operation():
    number1 = float
    number2 = float
    operation = str

    if operation == 'addition':
        return number1 + number2
    elif operation == 'substraction':
        return number1 - number2
    elif operation == 'multiplication':
        return number1 * number2
    elif operation == 'division':
        if number2 !=0:
            return number1 / number2
        else:
            return "Error: Division by zero."
    else:
        return "Error: Unsupported operation."
