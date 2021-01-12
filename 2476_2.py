mx_money=[]
for i in range(int(input())):
    l=list(map(int,input().split()))
    if l[0]==l[1]==l[2]:
        mx_money.append(10000+(1000*l[0]))
    elif l.count(l[0])==2:
        mx_money.append(1000+(100*l[0]))
    elif l.count(l[1])==2:
        mx_money.append(1000 + (100 * l[1]))
    else:
        mx_money.append(max(l)*100)
print(max(mx_money))