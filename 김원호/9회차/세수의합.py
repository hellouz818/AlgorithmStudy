import bisect
N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()
max_val = nums[-1]
num_sums = set()
for num1 in nums:
    for num2 in nums:
        if num1 + num2 > max_val:
            break
        num_sums.add(num1 + num2)

num_sums = list(num_sums)
num_sums.sort()
num_set = set(nums)
max_num = 0
for num_sum in num_sums[::-1]:
    idx = bisect.bisect_right(nums, max_val - num_sum)
    for num in nums[idx::-1]:
        num_sum3 = num + num_sum
        if num_sum3 > max_val:
            continue
        if num_sum3 < max_num:
            break
        if num_sum3 in num_set and num_sum3 > max_num:
            max_num = num_sum3

print(max_num)
