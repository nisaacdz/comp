t = int(input())

for _ in range(t):
    n = int(input())
    nums = input().split()

    res = []

    left, right = 0, n - 1
    start = True

    while left <= right:
        if start:
            res.append(nums[left])
            left += 1
        else:
            res.append(nums[right])
            right -= 1
        start = not start

    print(*res)
