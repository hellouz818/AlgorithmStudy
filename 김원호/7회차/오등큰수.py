"""
그냥 오등큰수를 구하는거 자체는 어렵지가 않은데
각 숫자마다 오등큰수를 구해야하면 시간복잡도가 O(N^2)이라서
좀 더 효율적인 방법을 찾아야해요
근데 생각해보면 첫번째 숫자의 오등큰수를 찾으려고 5번째 숫자까지 봤다고 치면
5번째숫자까지는 이미 훑었기 때문에 이때 뭔가 처리를 해주면
두번째 숫자의 오등큰수를 찾을때 5번째숫자까지는 그냥 건너뛰어도 될거같다는 생각이 들어요
거기에서 조금 더 확장해보면 각 숫자마다 오등큰수를 구하는 방법대신
리스트를 처음부터 끝까지 한번만 훑어서 모든 숫자의 오등큰수를 구할 수 있는 방법이 있지 않겠나 하는 생각이 들어요

리스트를 훑어보는 과정에서 지금 보고 있는 숫자가 A라고 했을때, 이 A가 오등큰수인 수는 더이상 기억하고 있을 필요가 없겠고,
이 A가 등장한 횟수가 A' 이면 지금까지 읽어들인 숫자중에 등장한 횟수가 A'보다 작은 숫자들이 오등큰수를 A로 가져요

그런데 등장한 횟수가 A'보다 큰지 작은지를 그냥 훑으려면 이것도 어차피 O(N^2)을 만들어서 지금까지 읽은 숫자중에
등장한 횟수가 A'보다 작은 숫자들을 빠르게 알아낼 수 있는 방법이 필요한데 이거는 이분탐색으로 구현하면 돼요

근데 글로만 쓰려니까 쓰기도 어렵고 읽고있기도 어려울거같아서 그냥 만나서 말씀드릴게요
"""
from collections import defaultdict
from bisect import bisect_left

_ = input()
nums = [int(x) for x in input().split()]
num2count = defaultdict(int)
for num in nums:
    num2count[num] += 1
counts = [num2count[num] for num in nums]

count2indices = defaultdict(list)
keys = []
ngfs = [-1 for _ in nums]
for i, count in enumerate(counts):
    idx = bisect_left(keys, count)
    if count not in count2indices:
        keys.insert(idx, count)
    count2indices[count].append(i)

    find_ngf_keys = keys[:idx]
    keys = keys[idx:]
    for find_ngf_key in find_ngf_keys:
        indices = count2indices[find_ngf_key]
        for index in indices:
            ngfs[index] = nums[i]
        del count2indices[find_ngf_key]

print(*ngfs)
