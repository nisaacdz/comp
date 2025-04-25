from bisect import bisect_left

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    paints = list(map(int, input().split()))
    paints.sort()

    res = 0

    for k in range(1, n):
        x = m - bisect_left(paints, k)
        y = m - bisect_left(paints, n - k)
        res += x * y - min(x, y)
    
    print(res)