N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [A[i] - B[i] for i in range(N)]

accumulatedC = [C[0]]
for i in range(1, N):
    accumulated_value = accumulatedC[-1] + C[i]
    accumulatedC.append(accumulated_value)

accumulated_value2count = {0: 1}
for accumulated_value in accumulatedC:
    if accumulated_value not in accumulated_value2count:
        accumulated_value2count[accumulated_value] = 0
    accumulated_value2count[accumulated_value] += 1

answer = 0
for count in accumulated_value2count.values():
    answer += count * (count - 1)
answer //= 2
print(answer)
