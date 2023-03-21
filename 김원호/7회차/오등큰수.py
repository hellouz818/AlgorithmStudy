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
