n = int(input())
nums = list(map(int, input().split()))
nums_sorted = sorted(nums)

sums = [0 for _ in range(n)]
mins = [0 for _ in range(n)]

sums[0] = nums[0]
mins[0] = nums_sorted[0]

for i in range(1, n):
    sums[i] = sums[i - 1] + nums[i]
    mins[i] = mins[i - 1] + nums_sorted[i]
    
m = int(input())

for _ in range(m):
    t, l, r = map(int, input().split())
    l, r = l - 1, r - 1

    res = 0
    if t == 1:
        res = sums[r] - (sums[l - 1] if l > 0 else 0)
    else:
        res = mins[r] - (mins[l - 1] if l > 0 else 0)
    
    print(res)