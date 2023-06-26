list = []
print("Для завершения ввода данных введите символ '='")
while True:
    b = []
    b = input().split()
    if b[0] != "=":
        if b[1] == "+":
            if b[0] not in list:
                list.append(b[0])
            else:
                list.copy()
        elif b[1] == "-":
            if b[0] in list:
                list.remove(b[0])
            else:
                list.copy()
    else:
        print(len(list))
        print(list)


