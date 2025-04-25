from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    nums = sorted(map(int, input().split()))

    freqs = []
    
    ans = True

    next = 0

    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i - 1]:
            if nums[i] != next:
                ans = False
            next += 1
            freqs.append(1)
        else:
            freqs[-1] += 1
    
    for i in range(1, len(freqs)):
        if freqs[i] > freqs[i - 1]:
            ans = False
            break
    
    print("YES" if ans else "NO")
