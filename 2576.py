l=list(filter(lambda x:x%2==1,[int(input()) for i in range(7)]))
if l:
    print(sum(l))
    print(min(l))
else:
    print(-1)