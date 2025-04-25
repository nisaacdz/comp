n = int(input())

d = 2 * n + 1

for i in range(0, n + 1):
    len = (2 * i) + 1
    print(' ' * (d - len), end='')
    print(" ".join(map(str, range(0, i + 1))), end='')
    if i > 0:
        print(' ', end='')
    print(" ".join(map(str, range(i - 1, -1, -1))).strip())
    
for i in range(n - 1, -1, -1):
    len = (2 * i) + 1
    print(' ' * (d - len), end='')
    print(" ".join(map(str, range(0, i + 1))), end='')
    if i > 0:
        print(' ', end='')
    print(" ".join(map(str, range(i - 1, -1, -1))).strip())