k = int(input())
op_list = input().split()
num = [0,1,2,3,4,5,6,7,8,9]
visited = [0] * 10
max, min = "", ""

def dfs(idx, string):
    global max, min

    if(idx == k+1):
        if(len(min) == 0):
            min = string
        else:
            max = string
        return

    for i in range(len(num)):
        if(visited[i] == 0):
            if(idx == 0 or ch(string[-1], str(i), op_list[idx-1])):
                visited[i] = 1
                dfs(idx+1, string+str(i))
                visited[i] = 0

# 새로 숫자가 추가될 때 앞에 숫자를 비교
def ch(i, j, bdh):
    if bdh == ">":
        return i > j # False
    else:
        print(i<j)
        return i < j # True

dfs(0, "")
print("%s\n%s" %(max, min))

'''
메모리/시간(Python3)
30616KB	132ms	
'''