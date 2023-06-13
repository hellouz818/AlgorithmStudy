import sys

input = sys.stdin.readline


def get_parent(x):
    if p[x] == x:
        return x
    p[x] = get_parent(p[x])
    return p[x]


def union(a, b):
    pa = get_parent(a)
    pb = get_parent(b)
    if pa > pb:
        union(b, a)
    p[pb] = pa


G = int(input())
P = int(input())
gi = [int(input()) for _ in range(P)]
p = [i for i in range(G+1)]

answer = -1
for num, g in enumerate(gi):
    pg = get_parent(g)
    if pg == 0:
        answer = num
        break
    union(pg-1, pg)

if answer == -1:
    answer = len(gi)
print(answer)
