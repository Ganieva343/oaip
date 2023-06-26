n = int(input())
m = input().split()
if len(m) != n:
    print('Количество чисел не соответствует заданному')
else:
    r = []
    for i in range(n):
        r.append(int(m[i]))
    r.sort()
    for i in range(n):
        if r[i] <= 1000:
            m = 0
        else:
            n = 0
    if n != 0:
        print(r)
    else:
        print('Условия задачи не соблюдены')
