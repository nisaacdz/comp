from collections import defaultdict


n, k = map(int, input().split())

nums = list(map(int, input().split()))

counts = defaultdict(int)

ans = (0, 0)

left, right = 0, 0

while left <= right and right < n:
    if len(counts) + (nums[right] not in counts) > k:
        counts[nums[left]] -= 1
        if counts[nums[left]] == 0:
            del counts[nums[left]]
        left += 1
    else:
        counts[nums[right]] += 1
        if right - left > ans[1] - ans[0]:
            ans = (left, right)
        right += 1

ans = (ans[0] + 1, ans[1] + 1)

print(*ans)
