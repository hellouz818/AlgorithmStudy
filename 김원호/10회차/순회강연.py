from collections import defaultdict
import heapq

n = int(input())
if n == 0:
    print(0)
    exit()
p_d = [[int(x) for x in input().split()] for _ in range(n)]
p_d.sort(key=lambda x: x[1], reverse=True)
day2pay = defaultdict(list)
for p, d in p_d:
    day2pay[d].append(p)
total_days = p_d[0][1]
possible_pays = []
answer = 0
for day in range(total_days, 0, -1):
    for payment in day2pay[day]:
        heapq.heappush(possible_pays, -payment)
    if possible_pays:
        answer -= heapq.heappop(possible_pays)
print(answer)
