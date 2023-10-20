

Ns = []
while True:
    N = int(input())
    if N == 0:
        break
    Ns.append(N)

max_N = max(Ns)
squares = []
for i in range(1, max_N + 1):
    square = i * i
    if square <= max_N:
        squares.append(square)
    else:
        break

dp = [[0 for _ in range(4)] for _ in range(max_N + 1)]
