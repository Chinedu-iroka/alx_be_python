num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operation = input("choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case"/":
        if num2 !=0:
            result = num1 / num2
        else:
            result = "Error: Division by zero is not allowed"
    case _:
        result = "Invalid operation selected"

print("The result is", result)

