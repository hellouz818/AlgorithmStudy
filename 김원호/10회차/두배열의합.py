from collections import defaultdict

T = int(input())
n = int(input())
A = [int(x) for x in input().split()]
m = int(input())
B = [int(x) for x in input().split()]
for i in range(1, n):
    A[i] += A[i-1]
for i in range(1, m):
    B[i] += B[i-1]
A = [0] + A
B = [0] + B
subtotal_count = {'A': defaultdict(int), 'B': defaultdict(int)}
for i in range(n):
    for j in range(i + 1, n + 1):
        subtotal = A[j] - A[i]
        subtotal_count['A'][subtotal] += 1
for i in range(m):
    for j in range(i + 1, m + 1):
        subtotal = B[j] - B[i]
        subtotal_count['B'][subtotal] += 1

answer = 0
for subtotal, A_count in subtotal_count['A'].items():
    if T - subtotal in subtotal_count['B']:
        answer += A_count * subtotal_count['B'][T - subtotal]
print(answer)
