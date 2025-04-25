t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()

    left, right = 0, n - 1

    total = 0

    while left < right:
        total += nums[right] - nums[left]
        left += 1
        right -= 1

    print(total)
