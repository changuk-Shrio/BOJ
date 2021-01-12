def find_me(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j]==9:
                return i,j

def can_go(size,me,b):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    cnt=[]
    for i in range(4):
        if b[me[0]+dy[i]][me[1]+dx[i]]<=size:
            cnt.append((me[0]+dy[i],me[1]+dx[i]))
    return cnt

def can_eat(size,b):
    eat=[]
    for i in range(len(b)):
        for j in range(len(b[0])):
            if 0<b[i][j]<size:
                eat.append((i,j))
    return eat

a=int(input())
b=[[] for i in range(a+2)]
b[0]=[10 for j in range(a+2)]
time=0
for i in range(1,a+1):
    b[i]=[10]+list(map(int,input().split()))+[10]
b[-1]=list(10 for i in range(a+2))

for i in b:
    print(i)
print()

s=0
for i in range(len(b)):
    s+=b[i].count(0)

if s==(a*a)-1:
    print(0)

else:
    size=2#아기상어기본크기
    me=find_me(b)#내장소찾아줌
    eat=can_eat(size,b)#먹을게 잇는지 없는지
    if len(eat)!=0:#먹을게있다
        cnt=can_go(size,me,b)#좌우앞뒤 움짐임 가능한지 확인
        if len(cnt)!=0:#움직일수있다
            pass


        else:#움직일수없다
            print(time)
    else:#먹을게 없다
        print(time)


#좌우앞뒤움직일수있는지확인?,작은거 찾고 거리가까운거
#먹을거 있는지과정필요 x
#갈수있는칸 다가봄 여기서 bfs 하다가 먹을거 걸리면 선정하고 움직임
#위 왼쪽 아래 오른쪽
#먹는거 나오면 다시 bfs