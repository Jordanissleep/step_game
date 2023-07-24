counter=0
while True:
    operation=input("enter password")
    num =(123)
    if operation =="123":
        print("welcome")
        break   
    else:
        print("password incorect")
        counter+=1
    if counter==5:
       print("your account is now locked")
       break