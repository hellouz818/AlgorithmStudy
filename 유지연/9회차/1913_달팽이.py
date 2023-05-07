N = int(input())

snail = [[0] * N for i in range(N)]

x_start = int((n - 1) // 2)
y_start= int((n - 1) // 2)
snail[x_start][y_start] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

...