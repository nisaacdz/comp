t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    twos = nums.count(2)
    b2 = 0
    k = 0
    for i in range(n):
        b2 += nums[i] == 2
        if b2 == twos - b2:
            k = i + 1
            break
    print(k if k else -1)
