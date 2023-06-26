r = []
e = input().split()
r.append(int(e[0]))
r.append(int(e[1]))
list = []
for i in range(1, r[0]+1):
    for t in range(1, r[1]+1):
        if len(list) > 0:
            if i % 2 == 0:
                list.append([i, r[1]+1-t])
            else:
                list.append([i, t])
        else:
            list.append([i, t])

for i in list:
    print(*i)

