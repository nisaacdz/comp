t = int(input())

for _ in range(t):
    n = int(input())
    vols = list(map(int, input().split()))
    
    decreasing = True

    for i in range(1, len(vols)):
        if vols[i] >= vols[i - 1]:
            decreasing = False
            break
    
    print("NO" if decreasing else "YES")