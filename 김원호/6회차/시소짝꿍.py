"""
같은 무게를 가지는 친구들은 항상 같은 짝궁이 되기때문에 따로 더해줌
같은 토크를 가지는 값들을 구하기 위해 dict를 사용
같은 토크를 가지는 값들이 여러개 있는 경우를 보면
a 무게가 x개
b 무게가 y개
c 무게가 z개
있다고 가정하면
짝궁이 될수있는 경우의 수는 xy + yz + zx 인데
이거는 (x(y+z) + y(z+x) + z(x+y)) // 2 랑 같음
s = x + y + z 라고 하면
(x(s-x) + y(s-y) + z(s-z)) // 2 로 사용가능
"""

from collections import defaultdict


def solution(weights):
    answer = 0
    weight2count = defaultdict(int)
    torque2weights = defaultdict(list)
    for weight in weights:
        weight2count[weight] += 1
        torque2weights[weight * 2].append(weight)
        torque2weights[weight * 3].append(weight)
        torque2weights[weight * 4].append(weight)

    for count in weight2count.values():
        answer += count * (count - 1) // 2

    same_torque_weight_pairs = set()
    for torque in torque2weights.keys():
        same_torque_weight_pairs.add(tuple(torque2weights[torque]))
    for pair in same_torque_weight_pairs:
        weights_in_pair = set(pair)
        # 1인 경우는 위에서 이미 계산했음
        if len(weights_in_pair) > 1:
            count_sum = 0
            for weight in weights_in_pair:
                count_sum += weight2count[weight]
            pair_sum = 0
            for weight in weights_in_pair:
                pair_sum += weight2count[weight] * (count_sum - weight2count[weight])
            answer += pair_sum // 2

    return answer
