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

seen = set()
with open('input2.txt', 'r') as file:
    # Read the contents of the file
    # content = file.read()
    lines = file.read().splitlines() # [goto 4, goto calc + 2 2,goto 2,goto 3]
    line_jumper = 1
    while lines[int(line_jumper) - 1] not in seen:
        value = (lines[line_jumper - 1]).split()
        seen.add(lines[int(line_jumper) - 1])
        if value[1] == 'calc':
            # print("calculating")
            operation = value[2]
            a=int(value[3])
            b=int(value[4])
            result = calculator(operation, a, b)
            line_jumper = int(result)
        else:
            # print("jumping")
            line_jumper = int(value[1])
    print(lines[int(line_jumper) - 1])

