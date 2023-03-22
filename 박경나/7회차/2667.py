import sys

N = int(sys.stdin.readline())
# N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip('\n'))))
    # graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
answer = []


def dfs(x, y):
    global cnt
    if x < 0 or x >= N or y < 0 or y >= N:  # 동서남
        return False

    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True


for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            answer.append(cnt)
            cnt = 0

print(len(answer))
answer.sort()
for i in answer:
    print(i)
