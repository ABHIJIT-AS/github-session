def add(x, y):
    """Adds two numbers"""
    return x + y

def subtract(x, y):
    """Subtracts two numbers"""
    return x - y

def multiply(x, y):
    """Multiplies two numbers"""
    return x * y

def divide(x, y):
    """Divides two numbers, with a check for division by zero"""
    if y == 0:
        return "Error! Cannot divide by zero."
    return x / y

def calculator():
    print("=== Simple Python Calculator ===")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    # Start a loop so the calculator keeps running until the user quits
    while True:
        choice = input("\nEnter choice (1/2/3/4) or 'q' to quit: ")

        # Check if the user wants to quit
        if choice.lower() == 'q':
            print("Exiting calculator. Goodbye!")
            break

        # Check if the choice is one of the valid operations
        if choice in ('1', '2', '3', '4'):
            try:
                # Ask the user for numbers and convert them to floats
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                # Handle cases where the user types letters or symbols instead of numbers
                print("Invalid input! Please enter numerical values.")
                continue

            # Perform the calculation based on user choice
            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid Input. Please select a valid operation.")
            
        print("-" * 30) # Print a divider for readability

# Run the program
if __name__ == "__main__":
    calculator()