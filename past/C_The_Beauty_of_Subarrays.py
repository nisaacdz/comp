t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    p1 = 0
    for i in range(n):
        if nums[i] == 1:
            p1 = i
            break
    left = p1 - 1
    right = p1 + 1
    found = [False for i in range(n + 1)]
    res = [0 for i in range(n)]
    found[1] = True
    needed = 2
    res[0] = 1
    while left >= 0 or right < n:
        if found[needed]:
            needed += 1
        elif left >= 0 and nums[left] == needed:
            found[needed] = True
            needed += 1
            left -= 1
        elif right < n and nums[right] == needed:
            found[needed] = True
            needed += 1
            right += 1
        elif left < 0:
            found[nums[right]] = True
            right += 1
        elif right >= n:
            found[nums[left]] = True
            left -= 1
        elif nums[left] < nums[right]:
            found[nums[left]] = True
            left -= 1
        else:
            found[nums[right]] = True
            right += 1
        print(res)
        res[(right - left - 1)] = 1 if needed == (right - left) else 0
    
    print("".join(res))
