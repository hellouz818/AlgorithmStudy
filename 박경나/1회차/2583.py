from collections import deque

m,n,k = map(int, input().split())
area = [[0] * n for i in range(m)]
cnt = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(k):
    x, y, x2, y2 = map(int, input().split())
    for j in range(y, y2):
        for k in range(x, x2):
            area[j][k] = 1

for i in range(m):
    for j in range(n):
        if area[i][j] == 0:
            ch = 1
            area[i][j] = 1
            dq = deque([[i, j]])
            
            while dq:
                x, y = dq[0][0], dq[0][1]
                dq.popleft()
                for k in range(4):
                    x1 = x + dx[k]
                    y1 = y + dy[k]
                    # 분리된 곳이 발견될 경우
                    if (0 <= x1 < m and 0 <= y1 < n):
                        if (area[x1][y1] == 0):
                            area[x1][y1] = 1
                            ch += 1
                            dq.append([x1, y1])
            cnt.append(ch)

print(len(cnt))
cnt.sort()
for i in cnt:
    print(i, end=' ')

'''
메모리/시간(Python3)
34144KB	76ms
'''