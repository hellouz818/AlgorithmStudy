import sys

sys.setrecursionlimit(10 ** 6)


def merge(p, q):
    pp, pq = get_parent(p), get_parent(q)
    parent[pp] = pq
    army_powers[pq] += army_powers[pp]
    army_powers[pp] = 0


def fight(p, q):
    pp, pq = get_parent(p), get_parent(q)
    ap, aq = army_powers[pp], army_powers[pq]
    if ap > aq:
        fight(q, p)
        return
    army_powers[pq] -= ap
    army_powers[pp] = 0
    if army_powers[pq]:
        merge(pp, pq)


def get_parent(a):
    if parent[a] != a:
        parent[a] = get_parent(parent[a])
    return parent[a]


N, M = map(int, input().split())
army_powers = [int(input()) for _ in range(N)]
parent = [i for i in range(N)]
for _ in range(M):
    O, P, Q = map(int, input().split())
    P -= 1
    Q -= 1
    if O == 1:
        merge(P, Q)
    else:
        fight(P, Q)
answer = []
for army_power in army_powers:
    if army_power:
        answer.append(army_power)
answer.sort()
print(len(answer))
print(*answer)
