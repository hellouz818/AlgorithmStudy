N = int(input())

def isPrime(n):
    if n == 1 :
        return False
    for i in range(2, int(n**(1/2))+1):
        if (n%i) == 0:
            return False
    return True

def dfs(num):
    if len(str(num))== N:
        print(num)
    else:
        for i in range(10):
            tmp = num*10+i
            if isPrime(tmp):
                dfs(tmp)


dfs(2) # 1000자리가 2
dfs(3)
dfs(5)
dfs(7)

"""
Result:
30616KB, 36ms, Python3
MEMO:
n자리까지 다 숫자 찾는게 아니라 1의 자리 소수맞는거부터 붙여나가는 방식
자리수 옮기는거 10곱하기!
isPrime에서 범위를 멍청하게 나눠서 길이가 조금 길어져서 수정했다. (1일때, 2일때, 2이상일때)
isPrime에서 int랑 범위 +1 안해줘서 틀렸었음
"""