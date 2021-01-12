import heapq
import sys

heap=[]
for i in range(int(input())):
    a=int(sys.stdin.readline())
    if a!=0:
        heapq.heappush(heap,a)
    else:
        if len(heap)==0 and a==0:
            print(0)
        else:
            print(heapq.heappop(heap))



