a=int(input())
print(" "*(a-1),end='')
print("*")
for i in range(1,a-1):
    print(" "*(a-1-i),end='')
    print("*",end='')
    print(" "*(2*i-1),end='')
    print("*")



if a!=1:
    print("*"*(a*2-1))