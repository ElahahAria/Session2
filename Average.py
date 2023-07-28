name = input("Please enter your name : ")
family = input("Please enter your family name : ")

Lesson1 = float(input("Lesson one Score  : "))
Lesson2 = float(input("Lesson two Score  : "))
Lesson3 = float(input("Lesson three score : "))

average = (Lesson1+Lesson2+Lesson3)/3

print(name, family)

if average >= 17:
    print("Status: Great")

if average >= 12 and average < 17:
    print("Status: Normal")

if average < 12:
    print("Status: Fail")
