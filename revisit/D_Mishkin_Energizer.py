t = int(input())

for _ in range(t):
    n = int(input())
    s = list(input())
    ops: list[int] = []

    def inspect():
        ilt = [0, 0, 0] # counts of l
        ilitlt = [-1, -1, -1] # il it lt -- position of one occurance

        for i in range(len(s)):
            if s[i] == 'I':
                ilt[0] += 1
                if i > 0 and s[i - 1] == 'L': # li
                    ilitlt[0] = i
                elif i > 0 and s[i - 1] == 'T': # ti
                    ilitlt[1] = i
            elif s[i] == 'L':
                ilt[1] += 1
                if i > 0 and s[i - 1] == 'I': # il
                    ilitlt[0] = i
                elif i > 0 and s[i - 1] == 'T': # tl
                    ilitlt[2] = i
            elif s[i] == 'T':
                ilt[2] += 1
                if i > 0 and s[i - 1] == 'I': # it
                    ilitlt[1] = i
                elif i > 0 and s[i - 1] == 'L': # lt
                    ilitlt[2] = i
            else:
                print("Hmmm, wierd")
        return ilt, ilitlt
    
    ins = inspect()

    if ins[0].count(0) > 1:
        print(-1)
        continue

    while max(ins[0]) != min(ins[0]):
        counts, ilitlt = ins
        print("".join(s))
        print("counts", counts)
        print("ilitlt", ilitlt)
        extremes = [min(counts), max(counts)]
        pos, m = (ilitlt[0], 'T') if sorted([counts[0], counts[1]]) == extremes else (ilitlt[1], 'L') if sorted([counts[0], counts[2]]) == extremes else (ilitlt[2], 'I')
        a, z = s[pos - 1], s[pos]
        s.insert(pos, m)
        s.insert(pos + 1, a)
        s.insert(pos, z)

        idxa = (a > 'I') + (a > 'L') + (a > 'T')

        if counts[idxa] == extremes[0]:
            s.insert(pos + 1, a)
        else:
            s.insert(pos + 2, z)

        ops.extend([pos, pos + 1, pos, pos + 1 if counts[idxa] == extremes[0] else pos + 2])

        ins = inspect()
    print(len(ops))
    for op in ops:
       print(op)

