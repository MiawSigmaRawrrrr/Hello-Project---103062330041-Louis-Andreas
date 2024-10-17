def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed"
def logarithm(x, base):
    if x > 0:
        return math.log(x, base)
    else:
        return "Error: Logarithm only defined for positive numbers"
    
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Logarithm")

    while True:
        choice = input("Enter choice(1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4', '5']:
            if choice == '5':
                num = float(input("Enter number: "))
                base = float(input("Enter base (use 10 for log base 10, or e for natural log): "))
                print(f"The result is: {logarithm(num, base)}")
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"The result is: {add(num1, num2)}")
                elif choice == '2':
                    print(f"The result is: {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"The result is: {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"The result is: {divide(num1, num2)}")
        else:
            print("Invalid input, please choose a valid operation.")

        # Ask if the user wants to perform another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

calculator()
