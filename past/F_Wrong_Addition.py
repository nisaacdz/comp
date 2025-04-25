t = int(input())

for _ in range(t):
    a, s = input().split()
    rem_zeros = len(s) - len(a)
    b = []
    sidx, aidx = len(s) - 1, len(a) - 1
    impossible = False
    while not impossible and sidx >= 0 and aidx >= 0:
        if s[sidx] >= a[aidx]:
            b.append(str(int(s[sidx]) - int(a[aidx])))
            sidx -= 1
            aidx -= 1
        elif sidx > 0 and 0 <= int(s[sidx - 1:sidx + 1]) - int(a[aidx]) < 10:
            b.append(str(int(s[sidx - 1:sidx + 1]) - int(a[aidx])))
            sidx -= 2
            aidx -= 1
        else:
            impossible = True
    if impossible or aidx >= 0:
        print(-1)
    else:
        if sidx >= 0:
            b.append(s[:sidx + 1])
        while len(b) > 1 and b[-1] == '0':
            b.pop()
        print(''.join(b[::-1]))