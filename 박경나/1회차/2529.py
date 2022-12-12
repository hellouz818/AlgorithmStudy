k = int(input())
op_list = input().split()
num = [0,1,2,3,4,5,6,7,8,9]
visited = [0] * 10
max, min = "", ""

def dfs(idx, string):
    global max, min

    if(idx == k+1):
        if(len(min) == 0):
            min = string # 처음 호출한 값
        else:
            max = string # 마지막 호출한 값
        return

    for i in range(len(num)):
        if(visited[i] == 0):
            if(idx == 0 or ch(string[-1], str(i), op_list[idx-1])):
                visited[i] = 1
                dfs(idx+1, string+str(i))
                visited[i] = 0

# 새로 숫자가 추가될 때 앞에 숫자를 비교
# 여기서 중복 방지 체크!
def ch(i, j, bdh):
    if bdh == "<":
        return i < j
    if bdh == ">":
        return i > j
    return True

dfs(0, "")
print("%s\n%s" %(max, min))

'''
메모리/시간(Python3)
30616KB	132ms

부등호를 더이상 만족하지 않으면 재귀함수를 할 필요가 없다 -> 가지치기

숫자, 부등호 담는 리스트 분리
부등호 인덱스 주의! 체크할 때 n과 n+1을 검사한다고 치면 인덱스 n-1해야함!

ch 함수 : 부등호 파악하는 함수이며 만약 j자리에 비교할 문자가 없는 경우 종료
'''