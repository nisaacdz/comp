t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    ans = [i for i in range(x)] + [i for i in range(x + 1, n)] + [i for i in range(x, min(n, x + 1))]
    print(*ans)