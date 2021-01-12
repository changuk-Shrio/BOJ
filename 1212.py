a=input()
l=[4,2,1]
chk=False
b=[[0 for i in range(3)] for j in range(len(a))]
for i in range(len(a)):
    c=int(a[i])
    for j in range(len(b)):
        if c>=l[j]:
            c-=l[j]
            b[i][j]=1
            chk = True
        if chk:
            print(b[i][j], end="")