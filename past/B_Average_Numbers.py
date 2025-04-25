n = int(input())
nums = list(map(int, input().split()))

total = sum(nums)
res = []
for i in range(n):
    if nums[i] == (total - nums[i]) / (n - 1):
        res.append(str(i + 1))

print(len(res))
print(" ".join(res))