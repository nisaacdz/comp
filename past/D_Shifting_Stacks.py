t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    for i in range(1, n):
        nums[i] += nums[i - 1]
    
    ans = True

    for i in range(n - 1, 0, -1):
        # n = i + 1
        # sn = (i + 1) i /2
        if nums[i] < (i * i + i) / 2:
            ans = False
            break
    
    print("YES" if ans else "NO")