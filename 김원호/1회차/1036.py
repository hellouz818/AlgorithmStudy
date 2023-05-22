'''
K개를 선택하는 문제로 접근
어떤 숫자를 Z로 바꾸었을때 숫자가 얼마나 커지는지를 계산해야한다. ... (1)
(1)을 계산하기 위해서 해당 숫자가 몇번 등장했는지 세는데, 이때 digit의 위치도 고려한다. ... (2)
예를들어서 10의 자리에 등장했으면 36번, 100의자리에 등장했으면 36 * 36번
해당 숫자와 Z의 차이만큼을 곱해서 얼마나 커지는지 계산한다. ... (3)
위에서 계산한 값을 기준으로 정렬해서 가장 큰 K개를 바꾸고, 기존 숫자의 합에 (3)에서 구한 값들을 더한후에 36진법으로 변환한다.
'''

from collections import Counter


def base36to10(base36: str) -> int:
    ret = 0
    for i, c in enumerate(base36[::-1]):
        ret += base36digit(c) * (36 ** i)
    return ret


def base36digit(base36: str) -> int:
    if base36.isnumeric():
        return int(base36)
    return ord(base36) - 55


def base10to36(base10: int) -> str:
    if base10 == 0:
        return 0
    ret = []
    while base10:
        base10, remain = divmod(base10, 36)
        ret.append(get_base36digit(remain))
    return ''.join(ret[::-1])


def get_base36digit(base10: int) -> str:
    if base10 < 10:
        return str(base10)
    return chr(base10 + 55)


N = int(input())
numbers = [input() for _ in range(N)]
K = int(input())

# 어떤 숫자가 몇번째 digit에 몇번 등장했는지 센다
num_digits = [[] for _ in range(max([len(num) for num in numbers]))]
for num in numbers:
    for i, c in enumerate(num[::-1]):
        num_digits[i].append(c)

# (2) 과정이고 final_counter가 해당 숫자가 몇번 등장했는지 가지게 된다.
num_counters = [Counter(num) for num in num_digits[::-1]]
for i, counter in enumerate(num_counters[:-1]):
    for _ in range(36):
        num_counters[i + 1] += counter
final_counter = num_counters[-1]

# (3) 과정이고 discriminator에 저장된 숫자는 해당 key를 Z로 바꿨을때 합이 얼마나 커지는지를 갖고있다.
discriminator = {}
for k, v in final_counter.items():
    discriminator[k] = (35 - base36digit(k)) * v

# (4) 과정이고 큰 순서대로 K개만 Z로 변환할것임
change_nums = [(k, v) for k, v in discriminator.items()]
change_nums.sort(key=lambda x: x[1], reverse=True)
change_nums = change_nums[:K]
change_nums = {k: v for k, v in change_nums}

answer = 0
for k, v in final_counter.items():
    final_counter[k] = v * base36to10(k)
    if k in change_nums:
        final_counter[k] += change_nums[k]
    answer += final_counter[k]
print(base10to36(answer))
