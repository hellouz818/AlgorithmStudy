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
        if len(weights_in_pair) > 1:
            count_sum = 0
            for weight in weights_in_pair:
                count_sum += weight2count[weight]
            pair_sum = 0
            for weight in weights_in_pair:
                pair_sum += weight2count[weight] * (count_sum - weight2count[weight])
            answer += pair_sum // 2

    return answer
