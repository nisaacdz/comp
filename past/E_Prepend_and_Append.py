t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    pos = 0

    while (n - (2 * pos) > 0) and s[pos] != s[n - pos - 1]:
        pos += 1
    
    print(n - (2 * pos))