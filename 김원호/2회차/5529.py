from collections import defaultdict
import heapq

import sys
sys.stdin = open('s')

M, N, K = map(int, input().split())
switches = [tuple([int(x) for x in input().split()]) for _ in range(K)] + [(M, N)]
row_dict = defaultdict(list)
col_dict = defaultdict(list)
for switch in switches:
    x, y = switch
    row_dict[x].append(switch)
    col_dict[y].append(switch)
heap = []
heapq.heappush(heap, (0, 1, 1, 0))
d2dict = {0: row_dict,
          1: col_dict}
distance = defaultdict(int)
distance[(1, 1)] = 10
while heap:
    t, x, y, d = heapq.heappop(heap)
    if x == M and y == N:
        print(-t - 1)
        print(distance)
        exit(0)
    if d == 0:
        num = x
    else:
        num = y
    for switch in d2dict[d][num]:
        nx, ny = switch
        nt = t - (1 + abs(nx - x) + abs(ny - y))
        if distance[(nx, ny)] == 0 or distance[(nx, ny)] > -nt:
            distance[(nx, ny)] = -nt
            heapq.heappush(heap, (nt, *switch, d ^ 1))

print(-1)
