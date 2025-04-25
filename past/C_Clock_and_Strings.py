t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())

    met_c = False
    met_d = False

    for num in range(min(a, b), max(a, b) + 1):
        if num == c:
            met_c = True
        if num == d:
            met_d = True
    
    cross = met_c ^ met_d

    print("YES" if cross else "NO")