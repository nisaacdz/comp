t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    res = [0 for _ in range(n)]
    
    largest, second = (0, 1) if nums[0] > nums[1] else (1, 0)

    for i in range(2, n):
        if nums[i] > nums[largest]:
            second = second if nums[second] > nums[largest] else largest
            largest = i
        elif nums[i] > nums[second]:
            second = i

    for i in range(n):
        if nums[i] == nums[largest]:
            res[i] = nums[i] - nums[second]
        else:
            res[i] = nums[i] - nums[largest]
            
    print(*res)