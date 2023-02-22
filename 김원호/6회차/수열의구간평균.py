"""
각 수에서 K값을 빼면 평균이 0인 구간을 찾는 문제로 바뀜
누적합이 같은 n, m이 있다고 하면 n+1 ~ m은 합이 0임

누적합이 같은 값을 가지는 인덱스가 x개 있으면 x 중 2개를 뽑는 경우의 수만큼 누적합이 0인 구간이 나옴
예를들어 1, 3, 5 번째 인덱스가 누적합이 모두 같은값이면
2~3, 2~5, 4~5 구간이 누적합이 0임

추가로 누적합이 0인 인덱스들은 다른 인덱스와 구간을 설정하지 않아도
그 자체로 조건을 만족하니까 한번 따로 더해줌
"""


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
    answer += value * (value - 1) // 2
answer += sum2index_count[0]

print(answer)
