for _ in range(int(input())):
    n = int(input())
    inputNums = map(int, input().split())

    nums = []

    for num in inputNums: # 1 1 1 2 3 3 4 5 6 6 6
        if len(nums) == 0 or nums[-1] != num:
            nums.append(num)
    
    valleys = 0

    for i in range(len(nums)):
        valleys += (i == 0 or nums[i - 1] > nums[i]) and (i == len(nums) - 1 or nums[i + 1] > nums[i])

    print("YES" if valleys == 1 else "NO")
