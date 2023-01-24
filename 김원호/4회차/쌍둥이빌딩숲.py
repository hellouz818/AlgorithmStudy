def solution(n, count):
    d = [[0] * (n + 1) for _ in range(n + 1)]
    d[1][1] = 1
    for i in range(1, n):
        for j in range(i, n):
            d[i + 1][j + 1] += d[i][j]
            d[i][j + 1] += d[i][j] * (2 * j)
    print(*d, sep='\n')
    answer = d[count][n]
    return answer
