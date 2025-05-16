s = input()
ans = []

while True:
    l, r = 0, len(s) - 1
    vals_l = []
    vals_r = []
    while l < r:
        while l < len(s) and s[l] != '(':
            l += 1
        while r >= 0 and s[r] != ')':
            r -= 1
        if l < r:
            vals_l.append(l)
            vals_r.append(r)
            l += 1
            r -= 1
    if not vals_l:
        break
    opp = [x + 1 for x in vals_l + vals_r[::-1]]
    ans.append(opp)
    s = ''.join([c for i, c in enumerate(s) if (i not in vals_l and i not in vals_r)])

print(len(ans))
for opp in ans:
    print(len(opp))
    print(' '.join(map(str, opp)))