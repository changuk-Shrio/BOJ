import collections
import sys
input=sys.stdin.readline

def dfs(i,j):
    global n
    a=collections.deque([[i,j]])
    while True:
        if len(a)==0:
            return l
        x,y=a.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if l[nx][ny]>n and visit[nx][ny]==0:
                a.append([nx,ny])
                visit[nx][ny]=1

n=int(input())
b=n
l=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
cnt=0
mx=0
l.append([0 for i in range(n+2)])
for i in range(n):
    a=list(map(int,input().split()))
    l.append([0]+a+[0])
    if max(a)>mx:
        mx=max(a)
l.append([0 for i in range(n+2)])


ll=[]
for k in range(0,mx+1):
    n=k
    visit=[[0 for _ in range(b+2)] for _ in range(b+2)]
    cnt=0

    for i in range(1,len(l)-1):
        for j in range(1,len(l)-1):
            if l[i][j]>n and visit[i][j]==0:
                l=dfs(i,j)
                cnt+=1
    ll.append(cnt)

    if cnt==0:
        break
print(max(ll))