a=int(input())
print("*")
for i in range(2,a+1):
    for j in range(i):
        print("*",end='')
    print()