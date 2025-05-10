t = int(input())

for _ in range(t):
    x = int(input())

    possible = False

    if x <= 1:
        print("NO")
        continue

    for a in range(1, int(pow(x, 1/3)) + 1):
        b = x - (a * a * a)
        br = pow(b, 1/3)

        br_int = int(round(br))

        if b > 0 and (br_int * br_int * br_int) == b:
            possible = True
            break
    
    print("YES" if possible else "NO")