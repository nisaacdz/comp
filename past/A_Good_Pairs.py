t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    largest = max(nums)
    smallest = min(nums)

    print(nums.index(smallest) + 1, nums.index(largest) + 1, sep=" ")