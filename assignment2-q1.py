import math

op = input("Enter operation (+,-,*,/,tan,sin,cos,cot,factorial,radical) = ")
a = int(input("Enter a = "))
b = int(input("Enter b = "))


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


if op == "sin":
    result = math.sin(a)


if op == "cos":
    result = math.cos(a)


if op == "tan":
    result = math.tan(a)

if op == "cot":
    result = math.cos(a)/math.sin(a)


if op == "factorial":
    if a>=0:
        result = math.factorial(a)


if op == "radical":
    if a>=0:
        result = math.sqrt(a)



print(result)
