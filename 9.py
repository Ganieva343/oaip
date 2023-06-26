n, m = map(int, input().split())
matrix = []
for i in range(n):
    r = []
    s = input().split()
    for i in range(m):
        r.append(int(s[i]))
    matrix.append(r)

sum = 0
for i in range(n):
    h = 0
    for t in range(m):
        h += (matrix[i])[t]
    if h >= sum:
        sum = h
        s = i + 1
print(s)
