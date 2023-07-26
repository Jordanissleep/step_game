num1=int(input("choose value 1= "))
num2=int(input("choose value 2= "))
num3=int(input("choose value 3= "))
if num1>num2 and num1>num3:
    print("the greatest is " + str(num1))
    if num2>num3:
       print("the middle is " + str(num2))
       print("the smallest is " + str(num3))
    else:
       print("the middle is " + str(num3))
       print("the smallest is " + str(num2))
if num2>num3 and num2>num1:
    print("the greatest is " + str(num2))
    if num3>num1:
       print("the middle is " + str(num3))
       print("the smallest is " + str(num1))
    else:
       print("the middle is " + str(num1))
       print("the smallest is " + str(num3))
if num3>num1 and num3>num2:
    print("the greatest is " + str(num3))
    if num1>num2:
       print("the middle is " + str(num1))
       print("the smallest is " + str(num2))
    else:
       print("the middle is " + str(num2))
       print("the smallest is " + str(num1))
else:
    print("YOU CANT DO THAT!")