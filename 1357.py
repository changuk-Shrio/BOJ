a, b = map(str, input().split())
s = str(int(a[::-1]) + int(b[::-1]))
print(int(s[::-1]))