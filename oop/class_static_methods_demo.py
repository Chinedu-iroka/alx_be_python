class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method
    @staticmethod
    def add(a, b):
        return a + b

    # Class method
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Example usage
if __name__ == "__main__":
    # Using static method
    sum_result = Calculator.add(10, 5)
    print(f"Sum: {sum_result}")  # Output: Sum: 15

    # Using class method
    product_result = Calculator.multiply(10, 5)
    print(f"Product: {product_result}")  # Output: Product: 50