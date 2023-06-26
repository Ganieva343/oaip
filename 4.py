n = int(input())
list = []
for i in range(1, n+1):
    if n % i == 0:
        list.append(i)
if len(list) > 2:
    print('NO')
else:
    print('YES')
