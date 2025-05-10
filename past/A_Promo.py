n, q = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort(reverse=True)

prev = 0
for i in range(n):
    cur = prev
    prev = nums[i] + cur
    nums[i] = cur

nums.append(prev)

for _ in range(q):
    x, y = map(int, input().split())

    ans = nums[x] - nums[x - y]
    print(ans)