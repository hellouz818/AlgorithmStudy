"""
시간시간이 빠른 순서대로 정렬한 다음
사람이 들어오면 컴퓨터를 할당해준다.
할당해줄때는 1번컴퓨터부터 훑으면서 해당 컴퓨터의 마지막사용자의 끝난 시간이 자신의 시작시간보다 작은 컴퓨터를 찾아서 할당함
할당할때 자신의 끝나는 시간을 해당 컴퓨터에 기록해둔다.

처음에는 이 논리로 시간초과날거같아서 다른방법을 열심히 고민해봣는데 아무리 생각해도 더 좋은방법이 잘 생각이 안나서
다른사람들 풀이 봤더니 다 이렇게 풀어서 당황함
"""

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
