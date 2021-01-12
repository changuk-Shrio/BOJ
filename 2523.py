a=int(input())
if a==1:
    print("*")
else:

    print("*")
    for i in range(2,a):
        for j in range(i):
            print("*",end='')
        print()
    for i in range(a-1,-1,-1):
        for j in range(i,-1,-1):
            print("*",end='')
        print()