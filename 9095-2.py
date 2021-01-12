li=[1,2,4]
for i in range(int(input())):
    a=int(input())
    if a<=len(li):
        print(li[a-1])
    else:
        for j in range(a-len(li)):
            li.append(sum(li[-3:]))
    print(li)