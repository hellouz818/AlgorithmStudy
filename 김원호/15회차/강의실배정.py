from collections import defaultdict

N = int(input())
times = defaultdict(int)
for n in range(N):
    s, e = map(int, input().split())
    times[s] += 1
    times[e] -= 1

keys = sorted(list(times.keys()))

room = 0
max_room = 0
for key in keys:
    room += times[key]
    if room > max_room:
        max_room = room
print(max_room)
