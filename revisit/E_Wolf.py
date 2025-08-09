t = int(input())

for _ in range(t):
    n, q = map(int, input().split())

    nums = list(map(int, input().split()))
    pos = dict((nums[i], i) for i in range(n))

    res: list[int] = []

    for _ in range(q):
        l, r, k = map(int, input().split())
        l, r = l - 1, r - 1
        x = pos[k]
        sG, sL = 0, 0
        uG, uL = 0, 0

        if x < l or x > r:
            res.append(-1)
            continue

        while l < r:
            m = (l + r) // 2
            
            if m == x:
                break
            
            if nums[m] > k and x > m:
                sL += 1
            elif nums[m] < k and x < m:
                sG += 1
            elif nums[m] > k:
                uG += 1
            elif nums[m] < k:
                uL += 1
            
            if x > m:
                l = m + 1
            else:
                r = m - 1
        
        ans = sG + sL + abs(sG - sL) if (sL < k - uL) and (n - k - uG >= sG) else -1
        res.append(ans)

    print(*res)
        