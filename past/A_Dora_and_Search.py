t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    mn , mx = 1, n

    left, right = 0, n - 1

    ans = []

    while left < right:
        if nums[left] == mn:
            left += 1
            mn += 1
        elif nums[left] == mx:
            left += 1
            mx -= 1
        elif nums[right] == mx:
            right -= 1
            mx -= 1
        elif nums[right] == mn:
            right -= 1
            mn += 1
        else:
            ans = [left + 1, right + 1]
            break
        
    if len(ans) == 2:
        print(*ans)
    else:
        print(-1)