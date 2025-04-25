t = int(input())

for _ in range(t):
    n = int(input())
    nums = sorted(map(int, input().split()))

    v = nums[-1] + sum(nums[2 * x] - nums[2 * x - 1] for x in range(1, n)) + nums[0]

    nums.append(nums[-1])

    nums[-2] = v

    print(*nums)