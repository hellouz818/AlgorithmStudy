import sys

def GoodOrBad(arr):
    arr_len = len(arr)				# 수열 길이
    for part_len in range(1, arr_len // 2 + 1):	# 비교할 부분수열의 길이
        # 부분수열 비교 시작
        for part_start in range(part_len, arr_len - part_len + 1):
            # 같은 부분수열 발견하면
            if arr[part_start - part_len:part_start] == arr[part_start:part_start + part_len]:
                return False			# False 리턴
    else:					# 모든 부분수열이 다르면
        return True				# True 리턴

# 백트래킹
def dfs(arr, depth):
    # 원하는 길이 -> 출력
    if depth == n:
        print("".join(list(map(str, arr))))
        sys.exit()

    arr.append(1)
    for i in range(1, 4):
        arr.pop()
        arr.append(i)
        if GoodOrBad(arr):			# 해당 수열이 좋은 수열이면
            if not dfs(arr, depth + 1):		# 다음 다리 수 시작
            # 만약 다음 자리 수에서 1~3 모두 넣어도 좋은 수열이 없다면
            # 현재 자릿수 1 증가
                continue
    else:
        # 현재 자릿수에 1~3 모두 넣어도 좋은 수열이 없는 경우
        arr.pop() # 이번 경우 빼기
        return False


n = int(input())
dfs([1], 1)

'''
30616KB	52ms
'''