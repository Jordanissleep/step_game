import random
number=random.randint(1,100)
counter=0
operator=input("enter name: ")
while True:
    operation=int(input("enter number: "))
    if number==operation:
       print("correct answer")
       break
    elif operation>number:
        print("Too High!")
        counter+=1
    elif operation<number:
        print("Too Low!")
        counter+=1
    
print(operator+" guessed "+str(counter))