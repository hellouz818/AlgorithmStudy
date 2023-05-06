'''
시간초과뜬 코드
억억단에서 몇번 등장했는지는 해당 숫자의 약수의 갯수와 같음
약수의 갯수를 구하기 위해서 먼저 소인수분해를 하고, 소인수분해 식에서 약수의 갯수를 구하는것을 이용함(이부분에서 시간이 오래걸려서 시간초과)
약수의 갯수를 전부 구하고나면 start 부터 e까지중에 가장 약수의 갯수가 많은 문제를 찾는걸로 바뀌기때문에
메모이제이션이 가능한데
f(n, e) := n부터 e까지 중에 약수의 갯수가 가장 많은 수
g(n) := n의 약수의 갯수
라고 하면
f(e, e) = e
f(n, e) = n if g(n) > g(f(n+1, e)) else f(n+1, e)
로 계산할 수 있다.
'''
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
