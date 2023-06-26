def factorization(n):
    p = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            p.append(d)
            n //= d
        d += 1
    if n >= 1:
        p.append(n)

    return p


a = factorization(int(input()))
b = []
g = []
for i in a:
    if i not in b:
        g.append(f'{i}^{a.count(i)}')
        b.append(i)
print("*".join(map(str, g)))