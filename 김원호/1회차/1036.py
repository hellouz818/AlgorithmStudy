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

num_digits = [[] for _ in range(max([len(num) for num in numbers]))]
for num in numbers:
    for i, c in enumerate(num[::-1]):
        num_digits[i].append(c)

num_counters = [Counter(num) for num in num_digits[::-1]]
for i, counter in enumerate(num_counters[:-1]):
    for _ in range(36):
        num_counters[i + 1] += counter
final_counter = num_counters[-1]

discriminator = {}
for k, v in final_counter.items():
    discriminator[k] = (35 - base36digit(k)) * v

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
