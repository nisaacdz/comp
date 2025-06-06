t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    a = input().split()
    b = input().split()

    count_a = [0 for _ in range(26)]
    count_b = [0 for _ in range(26)]

    for c in a:
        count_a[ord(c) - ord('a')] += 1

    for c in b:
        count_b[ord(c) - ord('a')] += 1

    def solve(arrs):
        c = []
        idx_1, idx_2 = 0, 0
        cur_count = 0
        while idx_1 < 26 or idx_2 < 26:
            if idx_1 < idx_2:
                
                pass
            else:
                pass
        
        return "".join(c)

    res_a = solve((count_a, count_b))
    res_b = solve((count_b, count_a))

    if res_a < res_b:
        print(res_a)
    else:
        print(res_b)