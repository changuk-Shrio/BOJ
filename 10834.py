l=[]
for i in range(int(input())):
   l.append(list(map(int,input().split())))
a=l[0][1]//l[0][0]#2번째바퀴

if l[0][-1]==0:
    d=1
else:
    d=-1

for i in range(1,len(l)):
    if l[i][0]==a:
        a=l[i][1]
    else:
        c=l[i][0]
        b=l[i][1]
        while l[i][0]!=a:
            l[i][0]+=c
            l[i][1]+=b
        a=l[i][1]
    if l[i][-1]==1:
        d*=-1

if d==1:
    print(0,a)
else:
    print(1,a)