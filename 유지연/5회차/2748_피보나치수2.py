N = int(input())
fibo = [i for i in range(N+1)]

fibo[1] = 1

for i in range(2, N+1) :
    fibo[i] = fibo[i-1] + fibo[i-2]
    
print(fibo[-1])

"""
Result 
113112KB, 116ms, Pypy3
Memo
"""