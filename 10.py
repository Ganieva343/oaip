n = int(input())
m1 = []
m2 = []
for i in range(n):
    r = []
    s = input().split()
    for i in range(n):
        r.append(int(s[i]))
    m1.append(r)
for i in range(n):
    r = []
    s = input().split()
    for i in range(n):
        r.append(int(s[i]))
    m2.append(r)
m3 = []
for i in range(n):
    r = []
    for t in range(n):
        r.append((m1[i])[t] + (m2[i])[t])
    m3.append(r)
for i in range(n):
    print(*m3[i])
