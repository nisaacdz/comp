t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    penalties = list(map(int, input().split()))

    def possible_complete(max_pen: int):
        ops = 0
        started = False
        for i in range(n):
            if s[i] == 'R':
                if started and penalties[i] > max_pen:
                    started = False
            else:
                if not started and penalties[i] > max_pen:
                    started = True
                    ops += 1

        return ops <= k

    low, high = 0, max(penalties)

    while low < high:
        mid = (low + high) // 2
        if possible_complete(mid):
            high = mid
        else:
            low = mid + 1
    
    print(low)
