n, t = map(int, input().split())

times = list(map(int, input().split()))

ans = 0


left, right = 0, 0
cur_time = 0

while right < n:
    if cur_time + times[right] > t:
        cur_time -= times[left]
        left += 1
    else:
        cur_time += times[right]
        right += 1
    ans = max(ans, right - left)

print(ans)