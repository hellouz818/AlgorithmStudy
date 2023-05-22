def is_prime(num):
    return primes[num]


def calc_score(num, name):
    if name == "daewoong":
        enemy = "gyuseong"
    else:
        enemy = "daewoong"
    if not is_prime(num):
        if len(maximum_3num[enemy]) < 3:
            score[enemy] += 1000
        else:
            score[enemy] += min(maximum_3num[enemy])
    elif num in numbers[name] or num in numbers[enemy]:
        score[name] -= 1000
    else:
        numbers[name].add(num)
        if len(maximum_3num[name]) < 3:
            maximum_3num[name].append(num)
        else:
            maximum_3num[name].append(num)
            maximum_3num[name].remove(min(maximum_3num[name]))


max_num = 5000000
primes = [True] * max_num
primes[0] = False
primes[1] = False
for i in range(2, int(max_num ** 0.5) + 1):
    if not primes[i]:
        continue
    for j in range(2 * i, max_num, i):
        primes[j] = False

names = ["daewoong", "gyuseong"]
score = {name: 0 for name in names}
numbers = {name: set() for name in names}
maximum_3num = {name: [] for name in names}

N = int(input())
for i in range(N):
    d, g = map(int, input().split())
    calc_score(d, names[0])
    calc_score(g, names[1])

if score[names[0]] > score[names[1]]:
    print("소수의 신 갓대웅")
elif score[names[0]] < score[names[1]]:
    print("소수 마스터 갓규성")
else:
    print("우열을 가릴 수 없음")
