n, q = map(int, input().split())
if q < n:
    print('0')
p = {}
for i in range(1, 7):
    p[1, i] = 1
for i in range(7, q+1):
    p[1, i] = 0
for i in range(2, n+1):
    for t in range(1, q+1):
        if t < i:
            p[i, t] = 0
        else:
            sum = 0
            for s in range(1, 7):
                if (t - s) > 0:
                    sum += p[i-1, t-s]
            p[i, t] = sum
print(float(p[n, q]/(6**n)))