def calculator(operation, a, b): 
    if operation == '+': 
        return a + b 
    elif operation == '-': 
        return a - b 
    elif operation == 'x': 
        return a * b 
    elif operation == '/': 
        if b != 0: 
            return a / b 
        else: 
            return "Error: Division by zero"
    else:
        return "Invalid operation"
    

# Get input from the user 
operation = input("Enter an operation (x, +, -, /): ")
a = int(input("Enter the first number: ")) 
b = int(input("Enter the second number: ")) 
#Calculate the result
result = calculator(operation, a, b) 

# Print the result 
print(f"The result of {a} {operation} {b} is: {result}")

