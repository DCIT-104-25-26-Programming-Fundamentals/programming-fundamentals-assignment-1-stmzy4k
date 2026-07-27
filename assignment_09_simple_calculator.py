def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    return a % b


def exponent(a, b):
    return a ** b


def display_menu():
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


while True:
    display_menu()

    choice = input("Select an operation (1-7): ")

    if choice == "7":
        print("Goodbye!")
        break

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Error: Invalid choice.")
        continue

    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    if choice == "1":
        result = add(first_number, second_number)
        print(f"Result: {first_number} + {second_number} = {result}")

    elif choice == "2":
        result = subtract(first_number, second_number)
        print(f"Result: {first_number} - {second_number} = {result}")

    elif choice == "3":
        result = multiply(first_number, second_number)
        print(f"Result: {first_number} * {second_number} = {result}")

    elif choice == "4":
        result = divide(first_number, second_number)

        if result is None:
            print("Error: Cannot divide by zero.")
        else:
            print(f"Result: {first_number} / {second_number} = {result}")

    elif choice == "5":
        result = modulus(first_number, second_number)
        print(f"Result: {first_number} % {second_number} = {result}")

    elif choice == "6":
        result = exponent(first_number, second_number)
        print(f"Result: {first_number} ** {second_number} = {result}")