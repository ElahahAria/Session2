a1 = float(input("enter side one : "))
a2 = float(input("enter side two : "))
a3 = float(input("enter side three : "))


max=max(a1,a2,a3)

if max==a1:
    if a2+a3>max :
        print("OK")
    else :
        print("NOT OK")
elif max==a2:
    if a1+a3>max :
        print("OK")
    else :
        print("NOT OK")
else:
    if a2+a1>max :
        print("OK")
    else :
        print("NOT OK")
