import math

a = int(input("Enter a = "))
b = int(input("Enter b = "))
op = input("Enter operation = ")

if op == "+":
    result = a + b


if op == "-":
    result = a - b


if op == "*":
    result = a * b


if op == "/":
    if b == 0:
        result = "Error"
    else:
        result = a / b


if op == "radical":
    result = math.sqrt(a)


if op == "sin":
    result = math.sin(a)


if op == "cos":
    result = math.cos(a)


if op == "tan":
    result = math.tan(a)


if op == "factorial":
    result = math.factorial(a)


if op == "cot":
    result = math.cos(a)/math.sin(a)


print(result)