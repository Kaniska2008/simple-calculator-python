
while True:
    print("\n===== SIMPLE CALCULATOR =====")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero!")

            again = input("Do you want to calculate again? (yes/no): ")

            if again.lower() == "no":
                print("Thank you for using the calculator!")
                break
            else:
                continue

        result = num1 / num2

    else:
        print("Invalid operator!")

        again = input("Do you want to calculate again? (yes/no): ")

        if again.lower() == "no":
            print("Thank you for using the calculator!")
            break
        else:
            continue

    print("Result =", result)

    again = input("Do you want to calculate again? (yes/no): ")

    if again.lower() == "no":
       print("Thank you for using the calculator!")
       input("\nPress Enter to exit...")
       break
    
