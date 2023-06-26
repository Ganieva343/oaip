from itertools import permutations
w = int(input())
a = input()

list = []
a = (''.join(map(str, a)))
a = sorted(a, reverse=True)
a = int(''.join(a))

def sum_digits(a):
    s = 0
    sum = 0
    while a >= 10:
        s = a % 10
        sum += s
        a //= 10
        list.append(s)
    list.append(a)
    sum += a
    list.append(sum)
    return list

list = sum_digits(a)
sum = list[w]
list.remove(sum)
l = len(list)
if l > w or l < w:
    print("Число не соответствует заданной величине")
else:
    list.sort()
    list.reverse()
    u = 0
    q = 0
    for i in list:
        if (i == 5) or (i == 0):
            while sum % 3 != 0:
                с = a - ((a // 3) * 3)
                b = str(с)
                if b in list:
                    list.remove(b)
                    print(list)
                while b not in list:
                    с = a - (((a - (с + 1)) // 3) * 3)
                    b = str(с)
                    if b in list:
                        list.remove(b)
                        print(list)
            else:
                u += 0
        else:
            u += 1
    if (u == l):
        print("impossible")
    else:
        hor = []

        for t in range(l):
            if len(hor) == 0:
                for i in permutations(list, r=(l - t)):
                    i = int(''.join(map(str,i)))
                    if i % 15 == 0:
                        hor.append(i)
        print(max(hor))