matrix = [[15, 20, 40, 85], [20, 35, 80, 95], [30, 55, 95, 105], [40, 80, 100, 120]]
n = int(input())

for i in range(4):
    for k in range(4):
        if matrix[i][k] == n:
            print(i, k)