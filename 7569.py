import collections
import sys
input=sys.stdin.readline
import time
def chk():
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 0:
                    return False
    return True

dx=[1,-1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]
max=0
m,n,h=map(int,input().split())
box=[[] for i in range(h)]
count=[0,0]
day=[[] for j in range(h)]
for i in range(h):
    for j in range(n):
        box[i].append(list(map(int,input().split())))
        day[i].append(list(0 for i in range(m)))
my=collections.deque([])
for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x]==1:
                my.append([z,y,x])
                day[z][y][x]=1



visit=[]
while len(my) != 0:
    ck=False
    z, y, x = my.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
            if box[nz][ny][nx] == 0:
                box[nz][ny][nx] = 1
                day[nz][ny][nx]+=day[z][y][x]+1
                my.append([nz,ny,nx])
    max=day[z][y][x]

if chk():
    print(max-1)
else:
    print(-1)
