for _ in range(int(input())):
    a, b, c, d = map(int, input().split())

    ans = 0
    ans += b > a
    ans += c > a
    ans += d > a

    print(ans)