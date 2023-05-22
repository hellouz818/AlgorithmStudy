from sys import stdin
input = stdin.readline
N = int(input())
rows = []
for _ in range(N):
    rows.append([int(x) for x in input().split()])
rows.sort(reverse=True)
max_height = 0
answer = 0
for width, height in rows:
    if height <= max_height:
        continue
    answer += width * (height - max_height)
    max_height = height
print(answer)
