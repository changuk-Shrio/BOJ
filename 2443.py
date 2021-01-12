a=int(input())
b=1
for i in range(a):
    print(" "*i,end="")
    print("*"*((2*a)-b))
    b+=2