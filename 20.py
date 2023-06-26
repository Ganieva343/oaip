m, n, t = map(int, input().split())
if m < n:
    if t % m == 0:
        print(t//m)
    else:
        print(t//m, t%m)
else:
    if t % n == 0:
        print(t//n)
    else:
        print(t//n, t%n)
