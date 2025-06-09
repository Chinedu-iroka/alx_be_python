def perform_operation(num1: float, num2: float, operation: str):
    if operation == 'addition':
        return num1 + num2
    elif operation == 'substraction':
        return num1 - num2
    elif operation == 'multiplication':
        return num1 * num2
    elif operation == 'division':
        if num2 !=0:
            return num1 / num2
        else:
            return "Error: Division by zero."
    else:
        return "Error: Unsupported operation."
