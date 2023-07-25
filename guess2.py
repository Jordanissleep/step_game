import random
number=random.randint(1,100)
low=1
high=100
mid=(low+high)/2
counter=0
while True:
    if number==mid:
        print("correct answer")
        break
    elif (number>mid):
        print("higher")
        low=mid+1
        counter+=1
    elif (number<mid):
        print("lower")
        high=mid-1