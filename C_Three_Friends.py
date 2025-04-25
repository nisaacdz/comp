for _ in range(int(input())):
    a, b, c = map(int, input().split())

    cur = abs(a - b) + abs(b - c) + abs(c - a)

    ans = cur - min(cur, 4)

    print(ans)