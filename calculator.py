def calculator():
    print("Welcome to the Simple Calculator!")
    
    #  user through input for the two numbers
    try:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return
    
    # Display operation choices
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter the operation (1/2/3/4): ")

    # Perform the calculation based on user input
    if operation == '1':
        result = n1 + n2
        print(f"The result of {n1} + {n2} is: {result}")
    elif operation == '2':
        result = n1 - n2
        print(f"The result of {n1} - {n2} is: {result}")
    elif operation == '3':
        result = n1 * n2
        print(f"The result of {n1} * {n2} is: {result}")
    elif operation == '4':
        if n2 != 0:
            result = n1 / n2
            print(f"The result of {n1} / {n2} is: {result}")
        else:
            print("Error: Cannot divide by zero.")
    else:
        print("Invalid operation selected.")

# Run the calculator
calculator()
