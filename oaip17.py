s = input()
n = len(s)
r = []
for i in s:
    r.append(i)
m = [0] * n
for i in range(n):
    c = r[i]
    if c in ['a', 'e', 'i', 'o', 'u']:
        r[i] = '0'
for i in range(n):
    if r[i] == '0':
        m[i] = 0
        for t in range(i, n+2):
            m[t+1] = m[t] + 1
    elif m[i] > 1:
        m[i]
    else:
        m[i] = 1
    n -= 1

print(m)
