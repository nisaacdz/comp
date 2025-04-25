n, s = map(int, input().split())
nums = list(map(int, input().split()))
left, right = 0, 0
cur_sum, max_len = 0, 0

while right < n:
    if cur_sum + nums[right] <= s:
        cur_sum += nums[right]
        right += 1
    else:
        cur_sum -= nums[left]
        left += 1
    max_len = max(max_len, right - left)

print(max_len)