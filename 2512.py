a=int(input())
money=list(map(int,input().split()))
tot=int(input())
tot_l=[]

if sum(money)<=tot:
    print(max(money))
else:
    big=max(money)
    sm=0
    mid=(big+sm)//2
    while True:
        total=0
        for i in range(len(money)):
            total+=money[i] if money[i]<=mid else mid
        if total<=tot:
            tot_l.append(mid)

        if total>tot:
            big=mid
            mid=(sm+big)//2
        elif total<=tot:
            sm=mid
            mid=(sm+big)//2

        if sm==mid or big==mid:
            break

    if len(tot_l)==0:
        print(0)
    else:
        print(max(tot_l))





