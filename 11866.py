import time
a,b=map(int,input().split())
l=[]
cnt=[1+i for i in range(a)]
chk=b
i=-1
j=0
while len(cnt)!=0:
    j+=1
    i+=1
    if j==b:
        j=0

print("<",end="")
for i in range(len(l)):
    print(l[i],end="")
    if i!=len(l)-1:
        print(", ",end="")
print(">")

print(4%6)
