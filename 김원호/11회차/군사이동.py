p, w = map(int, input().split())
c, v = map(int, input().split())

edges = [[int(x) for x in input().split()] for _ in range(w)]
parents = [x for x in range(p)]


def get_parents(x):
    if parents[x] != x:
        parents[x] = get_parents(parents[x])
    return parents[x]


def union(x, y):
    px = get_parents(x)
    py = get_parents(y)
    parents[px] = parents[py] = min(px, py)


edges.sort(key=lambda x: x[-1], reverse=True)
for ws, we, width in edges:
    union(ws, we)
    if get_parents(c) == get_parents(v):
        break
print(width)
