# REPL Calculator (within REPL)


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
button = input("Enter the operation (+, -, *, /): ")
if button == "+":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is {result}")
elif button == "-":
    result = num1 - num2
    print(f"The result of {num1} - {num2} is {result}")
elif button == "*":
    result = num1 * num2
    print(f"The result of {num1} * {num2} is {result}")
elif button == "/":
    result = num1 / num2
    print(f"The result of {num1} / {num2} is {result}")