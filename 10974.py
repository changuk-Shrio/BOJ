import itertools
a=[str(i+1) for i in range(int(input()))]
for i in list(itertools.permutations(a)):
    print(" ".join(i))