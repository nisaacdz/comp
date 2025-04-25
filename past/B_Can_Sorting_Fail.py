t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    mins = [nums[n - 1] for i in range(n)]
    maxs = [nums[0] for i in range(n)]
    maxs[0] = nums[0]
    mins[n - 1] = nums[n - 1]
    for i in range(1, n):
        maxs[i] = max(maxs[i - 1], nums[i])
    for j in range(n - 2, -1, -1):
        mins[j] = min(mins[j + 1], nums[j])
    found = False
    for i in range(1, n):
        if maxs[i - 1] <= mins[i]:
            found = True
            break
    print("NO" if found else "YES")