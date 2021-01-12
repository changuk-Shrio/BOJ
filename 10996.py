a=int(input())
if a==1:
    print("*")
else:
    for i in range(a):
        if a%2==0: print("* "*(a//2)+"\n"+" *"*(a//2))
        else: print("* "*(a//2+1)+"\n"+" *"*(a//2))


