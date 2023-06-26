x = input().split()
h = int(x[0])
m = int(x[1])
if (0 <= h <= 11) and (0 <= m <= 59):
    if (h != 0 and h != 6) and (m != 0 and m != 30):
        h = (h - 12) * -1
        m = (m - 60) * -1
        print(h, m)
    else:
        print(h, m)
else:
    print("Введены некоректные данные")
