t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    c = n - 1
    while c >= 0 and s[c] == ')':
        c -= 1
    print("No" if c + 1 >= n - c - 1 else "Yes")