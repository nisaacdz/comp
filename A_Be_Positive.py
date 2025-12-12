t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    zeros, positives, negatives = 0, 0, 0

    for num in nums:
        zeros += num == 0
        positives += num > 0
        negatives += num < 0
    
    ans = zeros + 2 * (negatives % 2)

    print(ans)