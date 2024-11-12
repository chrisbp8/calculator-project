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
#operation = input("Enter an operation (x, +, -, /): ")
#a = int(input("Enter the first number: ")) 
#b = int(input("Enter the second number: ")) 
#Calculate the result
#result = calculator(operation, a, b) 

# Print the result 
#print(f"The result of {a} {operation} {b} is: {result}")

# read from the file 

# Open the file in read mode
sum=0
with open('input1.txt', 'r') as file:
    # Read the contents of the file
    #content = file.read()
    lines= file.read().splitlines()
    for line in lines:
        value = line.split()
        operation= value[1]
        a=int(value[2])
        b=int(value[3])
        #Calculate the result
        result = calculator(operation, a, b) 
        sum += result

        # Print the result 
        print(f"The result of {a} {operation} {b} is: {result}")
        print (f"{sum}")
