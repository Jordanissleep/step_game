num1 =int(input("enter num1 "))
num2 =int(input("enter num2 "))
operation=input("enter the operation=")
if operation =="+":
   print(num1 +num2 )
elif operation =="-":
   print("num1 -num2 ")
elif operation =="*":
   print(num1 *num2 )
elif operation =="/":
     if (num2==0):
        print("cant divide by zero")
     else:
          print(num1/num2)
else:
     print("invalid operation, please try again")