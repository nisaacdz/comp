t = int(input())

for _ in range(t):
    n = int(input())
    a_set = set()
    b_set = set()
    for a in map(int, input().split()):
        a_set.add(a)
    for b in map(int, input().split()):
        b_set.add(b)
    possible = len(a_set) * len(b_set) >= 3

    print("YES" if possible else "NO")