def solution(bridge_length, weight, truck_weights):
    cnt = len(truck_weights)
    progress = []  # 현재 다리를 지나고 있는 트럭의 무게
    done = []  # 다리 건넌 트럭의 무게
    time = 0

    while cnt != len(done):
        if truck_weights:
            # 현재 건너고 있는 트럭의 무게 + 내 트럭의 무게 < 다리가 견딜 수 있는 무게
            if (len(progress) < bridge_length):
                if (sum([i[0] for i in progress]) + truck_weights[0] <= weight):
                    progress.append([truck_weights.pop(0), 0])
        time += 1 # 시간 1초 더하기

        for i in range(len(progress)):
            progress[i][1] += 1

        if progress[0][1] >= bridge_length:
            done.append(progress[0][0])
            progress.pop(0)
    return (time + 1)