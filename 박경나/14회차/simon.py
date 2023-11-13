n = int(input())

for i in range(n):
    _input = list(map(str, input().split()))
    if _input[0] == 'Simon':
        if _input[1] == 'says':
            # 빈 문자열 + 뒤에 리스트..
            print("", " ".join(map(str, _input[2:])))
    else:
        continue