N = int(input())
sanggun_numbers = set(map(int,input().split()))
M = int(input())
numbers = list(map(int, input().split()))
result = [0 for _ in range(M)]

for i in range(len(numbers)):
    if numbers[i] in sanggun_numbers:
        result[i] = str(1)
    else:
        result[i] = str(0)


print(' '.join(result))



"""
Result
253824KB, 564ms, Pypy3

Memo
1트. [map(int,input().split()) for _ in range(N)] 이라는 말도 안되는 문법
2트. 마지막 출력문 리스트가 아니라 스트링으로 써줘야해서 틀림
3트. 시간초과 -> 2번째 라인까지는 있냐 없냐만 판단하면 되서 set으로 바꿔줌
"""

