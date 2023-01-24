num2pos = {0: (3, 1)}
for i in range(1, 10):
    x = (i - 1) // 3
    y = (i - 1) % 3
    num2pos[i] = (x, y)


def is_adjacent(a, b):
    pos_a_x, pos_a_y = num2pos[a]
    pos_b_x, pos_b_y = num2pos[b]
    return abs(pos_a_x - pos_b_x) <= 1 and abs(pos_a_y - pos_b_y) <= 1


def get_dist(a, b):
    pos_a_x, pos_a_y = num2pos[a]
    pos_b_x, pos_b_y = num2pos[b]
    return abs(pos_a_x - pos_b_x) + abs(pos_a_y - pos_b_y)


def get_weight(a, b):
    if is_adjacent(a, b):
        return get_dist(a, b) + 1
    min_dist = 10
    min_val = -1
    for i in range(10):
        if not is_adjacent(a, i):
            continue
        dist = get_dist(i, b)
        if dist < min_dist:
            min_dist = dist
            min_val = i
    return get_weight(a, min_val) + get_weight(min_val, b)


def solution(numbers):
    d = [[[None] * 10 for _ in range(10)] for _ in range(len(numbers) + 1)]
    d[0][4][6] = 0
    d[0][6][4] = 0
    for i, number in enumerate(numbers, 1):
        number = int(number)
        for j in range(10):
            if j == number:
                continue
            min_weight = 10000000
            for k in range(10):
                if d[i - 1][k][j] is None:
                    continue
                weight = d[i - 1][k][j] + get_weight(number, k)
                if weight < min_weight:
                    min_weight = weight
            if min_weight != 10000000:
                d[i][number][j] = min_weight
                d[i][j][number] = min_weight
    answer = 10000000
    last_num = int(numbers[-1])
    for i in range(10):
        if d[-1][i][last_num] is None:
            continue
        answer = min(answer, d[-1][i][last_num])
    return answer


numbers = "1756"
print(solution(numbers))
numbers = "5123"
print(solution(numbers))
