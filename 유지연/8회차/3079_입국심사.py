N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))


start, end = 0, max(arr) * M

result = max(arr) * M

while (start <= end):

    mid = (start + end) // 2

    total = 0
    for i in range(N):
        total += mid // arr[i]


    if (total >= M):
        end = mid - 1
        result = min(result, mid)
    else:
        start = mid + 1

print(result)




"""
Result
120136KB, 308ms, Pypy3

Memo
검색해봤음,, 
시작을 0으로, 끝을 입국심사대 중 최대시간 * 사람수
이분탐색을 통해 mid를 사람수로 나누어서 몫의 합이 사람 수 이상인지 아닌지,,
처음에 그리디,,? 같은걸로 풀면 되지 않을까 생각했는데 이분탐색 흠냐
"""