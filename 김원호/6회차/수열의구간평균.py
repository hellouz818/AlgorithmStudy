from collections import defaultdict


N, K = map(int, input().split())
numbers = [int(x) for x in input().split()]

accumulate_sums = [0]
for num in numbers:
    accumulate_sum = accumulate_sums[-1] + num - K
    accumulate_sums.append(accumulate_sum)
accumulate_sums = accumulate_sums[1:]

sum2index_count = defaultdict(int)

for idx, accumulate_sum in enumerate(accumulate_sums):
    sum2index_count[accumulate_sum] += 1

answer = 0
for key, value in sum2index_count.items():
    if key == 0:
        answer += value * (value + 1) // 2
    else:
        answer += value * (value - 1) // 2

print(answer)
