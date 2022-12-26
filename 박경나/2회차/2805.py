n,m = map(int, input().split())
height = list(map(int,input().split()))
s, e = 1, max(height)

while s <= e: # 인덱스가 같아질 떄까지 이분탐색
    mid = (s+e) // 2
    total = 0

    for tree in height:
        if tree > mid: # 나무가 절단기보다 높다면
            total += tree-mid # 자른다.

    # 자른 나무의 길이 비교
    if total >= m: # 더 잘릴 경우
       s = mid+1
    else: # 덜 잘릴 경우
        e = mid-1
print(e)

'''
149684KB 4680ms
이분 탐색 쓸 때 함수 형태로 만들어서 재귀로 호출해도 된다는 것을 알았다.
근데 나는 재귀 안쓰고 while로 돌렸다!

이분탐색 기본 형태
def BinarySearch(arr, val, low, high):
    if low > high:
        return False #해당 배열에 타겟 숫자 없음

    mid = (low + high) // 2 # 인덱스 기반으로 찾는 것

    if arr[mid] > val:
        return BinarySearch(arr, val, low, mid - 1) #수가 중앙 값보다 아래 있는 경우
    elif arr[mid] < val:
        return BinarySearch(arr, val, mid + 1, high) #수가 중앙 값보다 위에 있는 경우
    else:
        return True #아니면 숫자를 출력 -> return val
'''