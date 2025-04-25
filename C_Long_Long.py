t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    total = 0

    for num in nums:
        total += abs(num)

    start, end, ops = 0, 0, 0

    while end < n:
        met_neg = False
        while end < n and nums[end] <= 0:
            met_neg |= nums[end] < 0
            end += 1
        else:
            end += 1
            
        if met_neg:
            ops += 1
        
        start = end

    print(total, ops)   
