import sys


sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
MAP = [[int(x) for x in input()] for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, h, visit):
    visit |= set([(x, y)])
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if not(0 <= nx < N and 0 <= ny < M):
            continue
        if (nx, ny) in visit:
            continue
        if MAP[nx][ny] < h:
            dfs(nx, ny, h, visit)
    return visit


answer = 0
for h in range(2, 10):
    visit = set()
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if (i, j) in visit:
                continue
            if MAP[i][j] >= h:
                continue
            new_visit = dfs(i, j, h, set())
            visit |= new_visit
            go_to_ground = False
            for x, y in new_visit:
                if x == 0 or y == 0 or x == N - 1 or y == M - 1:
                    go_to_ground = True
                    break
            if not go_to_ground:
                answer += len(new_visit)
print(answer)
