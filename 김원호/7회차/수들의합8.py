"""
Ci = Ai - Bi 인 C 배열을 생각해보면
Ci ~ Cj 의 합이 0이면
Ai ~ Aj 의 합과 Bi ~ Bj의 합이 같다는 얘기에요
그래서 Ci ~ Cj 의 합이 0 이 나오는 구간이 몇개인지를 풀면 되는 문젠데,
이거는 6회차에서 수열의 구간 평균 문제랑 결국 같아져요
"""
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
