t = int(input())

for _ in range(t):
    s = input()
    c = 0
    for i in range(len(s)):
        if s[len(s) - i - 1] != ')':
            break
        else:
            c += 1
    print("Yes" if c > (len(s) - c) else "No")