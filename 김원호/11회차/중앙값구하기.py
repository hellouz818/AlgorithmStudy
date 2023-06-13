import sys

input = sys.stdin.readline

T = int(input())
for t in range(T):
    M = int(input())
    numbers = [[int(x) for x in input().split()] for _ in range((M // 10) + 1)]
    numbers = sum(numbers, [])
    sorted_numbers = []
    rets = []
    for i, number in enumerate(numbers):
        j = 0
        for j, sorted_number in enumerate(sorted_numbers):
            if sorted_number > number:
                break
        else:
            j += 1
        sorted_numbers.insert(j, number)
        if i % 2 == 0:
            rets.append(sorted_numbers[i // 2])
    print(i // 2 + 1)
    rets = [rets[i * 10: i * 10 + 10] for i in range((len(rets) // 10) + 1)]
    for ret in rets:
        print(*ret)
