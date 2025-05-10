t = int(input())

for _ in range(t):
    k = int(input())

    res = []

    def solve(z, x, y):
        if z == 0:
            return
        v = 1
        # 1 => 0, 2 => 1, 3 => 3
        while v * (v - 1) // 2 <= z:
            res.append(((x + v), y))
            v += 1
        
        rem = z - (v - 1) * (v - 2) // 2
        solve(rem, x + v, y + 1)
    
    if k == 0:
        res.extend([(0, 0), (1, 1)])
    else:
        solve(k, 0, 0)

    print(len(res))
    for p in res:
        print(*p)