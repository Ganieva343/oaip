n = int(input())
m = []
symbols = set()
for i in range(n):
    r = []
    s = input().split()
    for i in range(2):
        r.append(s[i])
        symbols.add(s[i])
    m.append(r)
p = {}
for i in symbols:
    p[i] = 0
for i in m:
    for t in i:
        if t == m.index([i][0]):
            p[m[i][0]] -= 1
        elif t == m.index([i][-1]):
            p[m[i][1]] += 1
print(p)



print(m)
