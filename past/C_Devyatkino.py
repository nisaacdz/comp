t = int(input())

for _ in range(t):
    val = int(input())    
    ans = 11

    cur = val % 10

    if cur >= 7:
        ans = min(ans, cur - 7)
    else:
        ans = min(ans, cur + 3)
    
    val = val // 10

    prev = cur

    while val > 0:
        cur = val % 10
        if cur >= 7:
            ans = min(ans, cur - 7)
        else:
            ans = min(ans, cur + 3)
            t = 7 - cur
            t += t > prev
            ans = min(ans, t)
        prev = cur
        val = val // 10
    
    print(ans)