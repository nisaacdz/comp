t = int(input())

for _ in range(t):
    n = int(input())

    it = map(int, input().split())

    odds: list[int] = []
    evens: list[int] = []
    isOdd = True

    for num in it:
        if isOdd:
            odds.append(num)
        else:
            evens.append(num)
        isOdd = not isOdd
    
    if n % 2 == 1:
        evens.append(-1)

    izz1 = sorted((i for i in range(len(odds))), key=lambda x: odds[x])
    izz2 = sorted((i for i in range(len(evens))), key=lambda x: evens[x])

    res1: list[int] = []
    res2: list[int] = []

    for i in range(len(odds)):
        res1.append(odds[izz1[i]])
        res1.append(evens[izz1[i]])
    
    for i in range(len(evens)):
        res2.append(odds[izz2[i]])
        res2.append(evens[izz2[i]])
    
    if n % 2 == 1:
        p = res1.index(-1)

        while p + 2 < len(res1):
            res1[p] = res1[p + 2]
            p += 2
        res1.pop()

        q = res2.index(-1)
        while q + 2 < len(res2):
            res2[q] = res2[q + 2]
            q += 2
        res2.pop()

    if res1 < res2:
        print(" ".join(map(str, res1)))
    else:
        print(" ".join(map(str, res2)))