n = int(input())

nums = list(map(int, input().split()))

product = 1
zeros = 0

ans = 0

for i in range(n):
    ans += abs(abs(nums[i]) - 1)

    zeros += nums[i] == 0

    if nums[i] < 0:
        product *= -1

if product == -1 and zeros == 0:
    ans += 2

print(ans)