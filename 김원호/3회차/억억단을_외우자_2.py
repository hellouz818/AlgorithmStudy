def solution(e, starts):
    answer = []
    num_divisor = [1 for _ in range(e + 1)]
    for i in range(2, e + 1):
        for j in range(i, e + 1, i):
            num_divisor[j] += 1
    max_dict = [1 for _ in range(e + 2)]
    min_val = min(starts)
    max_num = num_divisor[e]
    for i in range(e, min_val - 1, -1):
        if num_divisor[i] >= max_num:
            max_dict[i] = i
            max_num = num_divisor[i]
        else:
            max_dict[i] = max_dict[i+1]
    for start in starts:
        answer.append(max_dict[start])
    return answer


e = 5000000
starts = [1, 3, 7]
print(solution(e, starts))
