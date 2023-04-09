from collections import defaultdict
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 7)
input = stdin.readline

N, M = map(int, input().split())
bad_relation_dict = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    bad_relation_dict[a].append(b)
    bad_relation_dict[b].append(a)

visit = [0] * (N + 1)
team = [-1] * (N + 1)


def dfs(x, team_num):
    visit[x] = 1
    team[x] = team_num
    for y in bad_relation_dict[x]:
        if team[y] == team_num:
            return False
        if visit[y]:
            continue
        if not dfs(y, team_num ^ 1):
            return False
    return True

answer = 1
for key in bad_relation_dict.keys():
    if team[key] == -1:
        if not dfs(key, 0):
            answer = 0
            break
    else:
        if not dfs(key, team[key]):
            answer = 0
            break

print(answer)
