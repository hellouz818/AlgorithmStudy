import sys

input = sys.stdin.readline


def get_parents(x):
    if p[x] != x:
        p[x] = get_parents(p[x])
    return p[x]


def union(x, y):
    px = get_parents(x)
    py = get_parents(y)
    if py < px:
        union(y, x)
        return
    p[py] = px
    network[px] |= network[py]


T = int(input())
for t in range(T):
    F = int(input())
    name2id = {}
    p = []
    network = []
    for f in range(F):
        names = input().split()
        for name in names:
            if name not in name2id:
                id_ = len(name2id)
                name2id[name] = id_
                p.append(id_)
                network.append(set([id_]))

        ids = map(lambda x: name2id[x], names)
        pids = [get_parents(id_) for id_ in ids]
        union(*pids)
        network_num = max(map(lambda x: len(network[x]), pids))
        print(network_num)
