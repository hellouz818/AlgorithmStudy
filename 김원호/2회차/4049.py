import sys

sys.stdin = open('s')

import math


def get_answer(tensor):
    answer = 0
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if (i == 1 and j == 1) or (i == r and j == c):
                continue
            if not (r % i == 0 and c % j == 0):
                continue
            tmp_tensors = []
            batch_x = r // i
            batch_y = c // j
            for x in range(i):
                split_line = tensor[x * (batch_x):(x + 1) * batch_x]
                for y in range(j):
                    sliced_tensor = [line[y * batch_y:(y + 1) * batch_y] for line in split_line]
                    tmp_tensors.append(sum(sliced_tensor, []))
            if is_able_to_factorize(tmp_tensors):
                answer += 1
    return answer


def is_able_to_factorize(split_tensor):
    x = len(split_tensor)
    y = len(split_tensor[0])
    for i in range(1, x):
        ratio = split_tensor[0][0] / split_tensor[i][0]
        for j in range(1, y):
            if not math.isclose(split_tensor[0][j] / split_tensor[i][j], ratio):
                return False
    return True


while True:
    r, c = map(int, input().split())
    if r == 0 and c == 0:
        break
    tensor = [[int(x) for x in input().split()] for _ in range(r)]
    print(get_answer(tensor))




