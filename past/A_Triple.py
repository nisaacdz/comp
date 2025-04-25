from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    nums = sorted(map(int, input().split()))

    ans = -1
    count = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            count += 1
            if count == 3:
                ans = nums[i]
                break
        else:
            count = 1
    
    print(ans)