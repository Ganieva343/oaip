mass = []
print("Для завершения ввода данных введите символ '='")
while True:
    list = input().split()
    lists = []
    lists = list[3:6]
    if list[0] != "=":
        i = 0
        del list[3:6]
        for a in range(3):
            i += int(lists[a])
        i /= 3
        list.append(i)
        mass.append(list)
        def fs(t):
            f = t[0:3]
            s = t[3]
            return (-s, f)
        mass.sort(key=fs)
    else:
        print(mass)



for i in range(list):
    if i[0] != i[1]:
        i+1
        print(i)
    elif i[0] == i[1]:
        mass.append(i)
    else:
        break


