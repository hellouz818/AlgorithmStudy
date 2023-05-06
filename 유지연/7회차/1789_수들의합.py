s = int(input())
N = 0
result = 0
for i in range(1,s+1):
    result += i
    N += 1
    if(result > s):
        N -= 1
        break
print(N)

"""
Result
114328KB, 120ms, Pypy3

Memo
1부터 하나씩 더해나가다가 결과값이 넘는 수(N)가 있다면 그 전의 수(N-1)의 합보다는 크고 넘는 수(N)보다는 작을 것이기 때문
1부터 더해주는것도 서로 다른 N개의 자연수의 합으로 나타낸 수가 S이기 때문에 작은수부터 많이 더해야 서로 다른 자연수 개수인 N의 값이 커짐
"""