n = int(input())
matrix = []
for i in range(n):
    r = []
    s = input().split()
    for i in range(n):
        r.append(int(s[i]))
    matrix.append(r)

d1 = 0
d2 = 0
for i in range(n):
    d1 += (matrix[i])[i]
    d2 += (matrix[i])[n - i - 1]

print(d1, d2)
