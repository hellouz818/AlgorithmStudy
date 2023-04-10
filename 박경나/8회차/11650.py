# 45100kb	404ms
import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    [x, y] = map(int, sys.stdin.readline().split())
    arr.append([x, y])

result = sorted(arr)

for i in range(N):
    print(result[i][0], result[i][1])