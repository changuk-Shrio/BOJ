import time
import collections
def move(x,y,xmv,ymv,cnt):#xms가 dx,ymv가 dy
    while plate[x+xmv][y+ymv]!="#" and plate[x][y]!="O":#움직일곳이 벽이아니면서 내위치가 골인지점이 아니면
        x+=xmv
        y+=ymv
        cnt+=1
    return x,y,cnt


def cut(can_go):
    rx=can_go.popleft()
    ry = can_go.popleft()
    bx = can_go.popleft()
    by = can_go.popleft()
    cnt = can_go.popleft()
    return rx,ry,bx,by,cnt



def bfs(can_go):
    rx,ry,bx,by,cnt=cut(can_go)

    if cnt>10:
        print(-1)
        return

    for i in range(4):
        nrx,nry,r_mv=move(rx,ry,dx[i],dy[i],0)
        nbx,nby,b_mv=move(bx,by,dx[i],dy[i],0)
        if plate[nbx][nby]!="O":
            if plate[nrx][nry]=="O":
                print(cnt)
                return

            if nrx==nbx and nry==nby:
                if r_mv>b_mv:
                    nrx,nry=nrx-dx[i],nry-dy[i]
                else:
                    nbx,nby=nbx-dx[i],nby-dy[i]
        else:
            print(-1)


        print(nrx,nry,nbx,nby)



        can_go.append([nrx,nry,nbx,nby,cnt+1])



selo,galo=map(int,input().split())
plate=[[] for i in range(selo)]
rx,ry,bx,by=0,0,0,0
cnt=0
dx=[1,0,-1,0]#위,아래
dy=[0,-1,0,1]#왼쪽,오른쪽
visit=[]
for i in range(selo):
    plate[i]=list(map(str,input()))
    for j in range(len(plate[i])):
        if plate[i][j]=="R":
            rx,ry=i,j#빨
        elif plate[i][j]=="B":
            bx,by=i,j#파

can_go=collections.deque([rx,ry,bx,by,cnt])

for i in plate:
    print(i)

print(bfs(can_go))


#왔던길은 못가게
