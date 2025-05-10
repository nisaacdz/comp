from collections import Counter

t = int(input())

# 1 4 3 4 3 2 4 1
# 1 1 2 3 3 4 4 4

for _ in range(t):
    n = int(input())
    nums = sorted(list(map(int, input().split())))

    num, freq = nums[0], 1 # num = 3, freq = 2

    for i in range(1, n):
        if nums[i] == num:
            freq += 1
            if freq >= 3:
                break
        else:
            num = nums[i]
            freq = 1
    
    print(num if freq >= 3 else -1)

