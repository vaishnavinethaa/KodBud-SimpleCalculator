print("Welcome to Simple Calculator")

while True:

    print("\nChoose an Operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1-4): ")

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    if choice == "1":
        result = num1 + num2
        print("Result =", result)

    elif choice == "2":
        result = num1 - num2
        print("Result =", result)

    elif choice == "3":
        result = num1 * num2
        print("Result =", result)

    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print("Result =", result)
        else:
            print("Division by zero is not possible.")

    else:
        print("Invalid Choice")

    again = input("\nDo you want to calculate again? (yes/no): ").lower()

    if again == "no":
        print("Thank you for using the calculator!")
        break