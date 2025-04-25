from collections import Counter
t = int(input())
# [3, 3, 1, 4, 7, 9, 4, 2, 7, 9, 2, 4, 1]
# [1, 1, 2, 2, 3, 3, 4, 4, 4, 7, 7, 9, 9]
# pos = 0
# [1] -- freqs

for _ in range(t):
    n, k = map(int, input().split())
    nums = sorted(map(int, input().split()))
    freqs = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            freqs[len(freqs) - 1] += 1
        else:
            freqs.append(1)

    freqs.sort()
    idx = 0
    while idx < len(freqs) - 1 and freqs[idx] <= k:
        k -= freqs[idx]
        idx += 1
    
    res = len(freqs) - idx

    print(res)