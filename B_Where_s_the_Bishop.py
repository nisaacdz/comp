t = int(input().strip())

corners = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

for _ in range(t):
    mat = ["" for _ in range(8)]
    input()
    for i in range(8):
        mat[i] = input().strip()
    
    ans = (0, 0)
    for i in range(1, 7):
        for j in range(1, 7):
            if all(mat[i + x][j + y] == '#' for (x, y) in corners):
                ans = (i + 1, j + 1)
                break

    print(*ans)