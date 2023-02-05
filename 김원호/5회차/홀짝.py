def find_nth_group(num):
    s = 1
    e = 10 ** 100
    while s <= e:
        mid = (s + e) // 2
        if mid * (mid + 1) >= num * 2:
            e = mid -1
        else:
            s = mid + 1
    return s


N = int(input())
nth_group = find_nth_group(N)

print(N * 2 - nth_group)