t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    s = k - 1

    for i in range(k - 1, -1, -1):
        if nums[i] == n:
            s == i - 1
        else:
            break

    nums.sort()

    moves = n
    cur_pos = s
    cat_pos = 0

    while cur_pos >= 0 and n - nums[cur_pos] <= moves:
        moves -= n - nums[cur_pos]
        cur_pos -= 1
    
    print(n - cur_pos)