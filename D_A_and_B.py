t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    def group(c: str) -> int:
        count = 0
        start, end = -1, -1
        for i in range(len(s)):
            count += s[i] == c
            if start == -1 and s[i] == c:
                start = i
            if end == -1 and s[len(s) - i - 1] == c:
                end = len(s) - i - 1
        
        cur = 0
        ans = 0

        #print(c, count, start, end)

        for i in range(start, end + 1):
            if s[i] == c:
                cur += 1
            else:
                ans += min(cur, count - cur)
        
        return ans
    
    ans = min(group('a'), group('b'))

    print(ans)