# Display the calculator menu
print ("Welcome to the Basic Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get the user's choice
choice = input("choose an operation (1/2/3/4): ")

#Get two numbers from the user
num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))

# Perform the chosen operation
if choice == "1":
        print(f"the result of Addition: {num1+num2}")

elif choice == "2":
        print(f"the result of Subtraction: {num1-num2}")

elif choice == "3":
        print(f"the result of Multiplication: {num1*num2}")

elif choice == "4":
        if num2 != 0:
            print(f"the result of Division: {num1/num2}")
        else:
            print("Error: Division by zero is not allowed.")
else:
       print("Invalid Choice. Please select a valid option.")