t = int(input())

def solve(nums):
    cur = 0
    total = 0

    while cur < len(nums):
        largest = nums[cur]
        sign = nums[cur] > 0

        while cur < len(nums) and (nums[cur] > 0) == sign:
            largest = max(largest, nums[cur])
            cur += 1
        total += largest
        
    return total

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(solve(nums))
    
