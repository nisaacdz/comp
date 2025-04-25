t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    sum = 0
    i = 0

    while sum < k and i < len(a):
        sum += a[i]
        i += 1
        
    print(k - sum if sum <= k else k - sum + a[i - 1])