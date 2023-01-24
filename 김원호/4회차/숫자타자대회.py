"""
dp로 풀었어요
d[n][a][b] 는 n번째 숫자를 타이핑 한 뒤에 손가락이 a, b 숫자에 있을때의 최소 가중치를 뜻해요
왼손, 오른손은 굳이 의미가 없기때문에 d[n][a][b] = d[n][b][a]이고요 이 부분은
a가 b보다 작은경우만 다룬다거나 하는 등 다른 로직으로 처리할수도 있긴한데 그냥 d[n][a][b] = d[n][b][a]
가 제일 코딩하기 간편해서 이렇게했어요
n번째 숫자가 k라고 하면 k를 타이핑 한 뒤에는 두 손가락 중 한개는 k에 있어야 하기때문에
d[n][a][b] 에서 a == k 이거나 b == k를 만족해야해요
간단히 a == k를 만족하는 경우를 구하려고 보면
d[n][k][b] 를 구해야하는데 k번 자리에 있는 손가락이 그 전 단계에서 0~9중에 있었을것이기 때문에 그 전단계까지의 가중치는
d[n-1][0][b], d[n-1][1][b], ... , d[n-1][9][b]가 되고
이 각각의 값에 k번을 타이핑하는데 드는 가중치를 더한 값들중에 최솟값이 d[n][k][b]의 값이 됩니다
여기서 b는 아무 조건이 없기때문에 0~9까지(k는 빼고) 구해주면 돼요
"""

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
