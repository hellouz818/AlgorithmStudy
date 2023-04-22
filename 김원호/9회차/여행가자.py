from collections import defaultdict


def dfs(x, n):
    group[x] = n
    for y in bridges[x]:
        if group[y]:
            continue
        dfs(y, n)


N = int(input())
M = int(input())
bridges = defaultdict(list)
for i in range(N):
    bridges[i] = [j for j, x in enumerate(input().split()) if x == '1']
plan = [int(x) - 1 for x in input().split()]

group = [0 for _ in range(N)]
for i in range(N):
    if group[i]:
        continue
    dfs(i, i + 1)

plan_group = [group[p] for p in plan]

answer = 'YES'
discrimination = plan_group[0]
for p_group in plan_group:
    if p_group != discrimination:
        answer = 'NO'
        break
print(answer)
