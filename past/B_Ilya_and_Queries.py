s = input()
m = int(input())

ss = [0 for _ in range(len(s) + 1)]

for i in range(1, len(s)):
    ss[i] = ss[i - 1] + (s[i - 1] == s[i])

for _ in range(m):
    l, r = map(int, input().split())

    ans = ss[r - 1] - ss[l - 1]

    print(ans)