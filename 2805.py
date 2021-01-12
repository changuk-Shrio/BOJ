import time
n,m=map(int,input().split())
wood_len=list(map(int,input().split()))
low=0
high=max(wood_len)
ans=0
while low<=high:
    mid=(low+high)//2#mid를 출력하자
    tree_len=0
    for i in range(n):
        if wood_len[i]>mid:
            tree_len+=wood_len[i]-mid
    if tree_len>=m:
        ans=mid
        low=mid+1
    elif tree_len<m:
        high=mid-1
print(ans)