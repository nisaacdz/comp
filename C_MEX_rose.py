t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    nums = sorted(map(int, input().split()))

    present = [False for _ in range(k)]
    count_k = 0
    
    prev = -1
    
    for num in nums:
        if num >= 0 and num < k:
            present[num] = True
        elif num == k:
            count_k += 1

    ensure_present = 0
    
    for i in range(k):
        ensure_present += not present[i]

    ensure_absent = count_k

    ans = ensure_present + max(0, ensure_absent - ensure_present)

    print(ans)