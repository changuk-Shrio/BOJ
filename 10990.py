a=int(input())
print(" "*(a-1)+"*")
for i in range(0,a-1):
    print(" "*(a-i-2)+"*"+" "*(2*i+1)+"*")