t = int(input())

for _ in range(t):
    n, h = map(int, input().split())
    nums = list(map(int, input().split()))

    def could_kill(k: int) -> bool:
        damages = 0
        for i in range(n):
            if i == n - 1:
                damages += k
            else:
                end = min(nums[i] + k, nums[i + 1])
                damages += end - nums[i]
        return damages >= h
    
    low, high = 0, h

    while low < high:
        k = (low + high) // 2

        if could_kill(k):
            high = k
        else:
            low = k + 1
    
    print(low)