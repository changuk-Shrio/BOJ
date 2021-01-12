a=int(input())
for i in range(1,2*a):
    if i>a:print("*"*(a*2-i)+" "*(i*2-a*2)+"*"*(a*2-i))
    else: print("*"*i+" "*(a*2-(i*2))+"*"*i)



