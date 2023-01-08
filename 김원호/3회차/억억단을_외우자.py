from collections import Counter


def solution(e, starts):
    answer = []
    min_val = min(starts)
    num2num_divisors = {}
    primes = []
    for i in range(2, int(e ** 0.5) + 1):
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    for i in range(min_val, e+1):
        factorizations = []
        j = 0
        org_i = i
        while i > 1:
            if i % primes[j] == 0:
                i //= primes[j]
                factorizations.append(primes[j])
                continue
            j += 1
            if j == len(primes) or primes[j] > i:
                factorizations.append(i)
                break
        counter = Counter(factorizations)
        num_divisors = 1
        for v in counter.values():
            num_divisors *= (v+1)
        num2num_divisors[org_i] = num_divisors
    max_dict = {e+1: 0}
    num2num_divisors[0] = -1
    min_val = min(starts)
    for i in range(e, min_val - 1, -1):
        num = num2num_divisors[max_dict[i + 1]]
        if num2num_divisors[i] >= num:
            max_dict[i] = i
        else:
            max_dict[i] = max_dict[i+1]

    for start in starts:
        answer.append(max_dict[start])
    return answer


e = 8
starts = [1, 3, 7]
print(solution(e, starts))
