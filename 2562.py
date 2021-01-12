max=0
now=0
for i in range(9):
    a=int(input())
    if a>max:
        max=a
        now=i+1
print(max)
print(now)