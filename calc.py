n=int(input("enter value of range: "))
k=int(input("enter value of iteration: "))
a=pow(2,k)
b=n/a
c=n-b
print("eliminated: "+str(c))
print("remaining: "+str(b))