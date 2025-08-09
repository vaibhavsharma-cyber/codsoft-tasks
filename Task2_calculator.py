# Simple Calculator
# Created by Vaibhav Sharma

def display_menu():
    print("\n" + "-"*30)
    print("   SIMPLE CALCULATOR   ")
    print("-"*30)
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("5 - Exit")
    print("-"*30)

while True:
    display_menu()
    
    try:
        option = int(input("Choose an operation (1-5): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1-5.")
        continue

    if option == 5:
        print("You chose to exit. Goodbye!")
        break
    
    if option not in [1, 2, 3, 4]:
        print("Invalid option! Please choose 1-5.")
        continue

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        continue

    if option == 1:
        result = num1 + num2
        print(f"Addition of {num1} and {num2} is: {result}")

    elif option == 2:
        result = num1 - num2
        print(f"Subtraction of {num1} and {num2} is: {result}")

    elif option == 3:
        result = num1 * num2
        print(f"Multiplication of {num1} and {num2} is: {result}")

    elif option == 4:
        if num2 != 0:
            result = num1 / num2
            print(f"Division of {num1} by {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
