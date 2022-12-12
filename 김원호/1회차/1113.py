'''
처음에는 모든 위치에서 dfs를 돌면서 물이 갇히는지, 땅으로가는지(go_to_ground) 판단했는데 시간초과로 고생함
이렇게 하지말고 물의 수위(h)를 높여가면서 높이가 h보다 작은 위치에서만 dfs를 돌리면 된다.
'''
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
            # go_to_ground가 False이면 물이 갇힌상태이고 수영장이 되는데, new_visit에 있는 위치들이 수영장이 될수있는 장소이다
            # new_visit에 있는 원소들에 전부 물을 1씩 채우면 되기때문에 len(new_visit)을 더해주면 된다.
            # 만약에 물의 높이가 7이고 해당 땅의 높이가 1이면 6을 채워야하는데 왜 1씩 채우는지 궁금할수도 있는데
            # h가 2부터 시작했기때문에 h = 2, 3, 4, 5, 6, 7에서 각각 1씩 채워주면 6을 채워준거랑 같다.
            if not go_to_ground:
                answer += len(new_visit)
print(answer)
