"""
math.root나 ** 0.5는 숫자가 너무 커지면 계산이 부정확함
홀짝이 몇번 반복됐는지만 알면 쉽게 구할 수 있는데, 처음엔 이걸 수식 써서 찾았는데
이분탐색으로 찾아야 했음
"""

def find_nth_group(num):
    s = 1
    e = 10 ** 100
    while s <= e:
        mid = (s + e) // 2
        if mid * (mid + 1) >= num * 2:
            e = mid -1
        else:
            s = mid + 1
    return s


N = int(input())
nth_group = find_nth_group(N)

print(N * 2 - nth_group)