t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()

    ans = 0
    
    for i in range(0, len(nums), 2):
        ans = max(ans, abs(nums[i] - nums[i + 1]))

    print(ans)