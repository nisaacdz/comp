t = int(input())

for _ in range(t):
    n = int(input())

    equality = list(map(int, input().split()))

    possible = True

    for i in range(2, len(equality)):
        if equality[i - 2] == 1 and equality[i - 1] == 0 and equality[i] == 1:
            possible = False
            break

    print("YES" if possible else "NO")