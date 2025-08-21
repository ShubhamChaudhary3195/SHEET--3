num1 = int(input("enter the number"))
for i in range(1,num1+1):
    for j in range(num1+1-i):
        print("*",end = " ")
    print()