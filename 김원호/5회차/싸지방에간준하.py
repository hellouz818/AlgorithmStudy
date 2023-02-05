from collections import defaultdict


N = int(input())
end_times = [-1 for _ in range(N)]
count_dict = defaultdict(int)
Timestamps = []
for _ in range(N):
    Timestamps.append([int(x) for x in input().split()])
Timestamps.sort()

for s, e in Timestamps:
    for i, end_time in enumerate(end_times):
        if end_time < s:
            count_dict[i] += 1
            end_times[i] = e
            break

n = len(count_dict)
print(n)
print(*[v for v in count_dict.values()])
