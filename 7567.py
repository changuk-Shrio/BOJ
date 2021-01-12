a=input()
l=10
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        l+=5
    else:
        l+=10
print(l)