n = int(input())
nums = list(map(int, input().split()))

max_num = nums[0]
min_num = nums[0]
amazing = 0
for i in range(1, n):
    if nums[i] > max_num or nums[i] < min_num:
        max_num = max(max_num, nums[i])
        min_num = min(min_num, nums[i])
        amazing += 1

print(amazing)
