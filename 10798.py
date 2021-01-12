l = [input() for i in range(5)]
max_len = max([len(i) for i in l])
for i in range(max_len):
    for j in range(5):
        if len(l[j]) > i:
            print(l[j][i], end="")