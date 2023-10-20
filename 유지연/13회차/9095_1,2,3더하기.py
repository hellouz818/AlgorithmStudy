T = int(input())

for i in range(T) :
    n = int(input())
    dp = [0]*11
    if n == 1 :
        print(1)
    elif n == 2 :
        print(2)
    elif n == 3 :
        print(4)
    else :
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for j in range(4,n+1) :
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
        print(dp[n])

"""
Result
108080KB, 108ms, Pypy3

Memo
1+1+1+1, 2+1+1, 3+1, 1+2+1 (3만들기 + 1)
1+1+2, 2+2 (2만들기 + 2)
1+3 (1만들기 + 3)
4만들기 = 1만들기 + 2만들기 + 3만들기

f(n) = f(n-1) + f(n-2) + f(n-3) (n>=4) f(1)=1,f(2)=2,f(3)=4
"""