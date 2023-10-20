def dfs(digit_num, numbers):
    if digit_num == 0:
        return numbers
    if numbers:
        last_num = numbers[-1]
        if last_num == 0:
            return numbers
    else:
        last_num = 10
    ret = []
    for i in range(digit_num - 1, int(last_num)):
        if digit_num >= 2:
            ret.extend(dfs(digit_num - 1, numbers + f"{i}"))
        else:
            ret.append(dfs(digit_num - 1, numbers + f"{i}"))
    return ret


N = int(input())
decreasing_numbers = []
for i in range(1, 11):
    decreasing_numbers.extend(dfs(i, ""))
    if len(decreasing_numbers) >= N:
        print(decreasing_numbers[N-1])
        break
else:
    print(-1)
