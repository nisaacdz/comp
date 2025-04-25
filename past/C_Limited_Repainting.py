t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    colors = input()
    penalties = list(map(int, input().split()))
    low = 0, high = max(penalties)

    def canPaintWithMaxPenalty(maxPenalty: int) -> bool:
        tries = k
        for i in range(1, n):
            pass
        return True

    while low < high:
        mid = (low + high) / 2
        if canPaintWithMaxPenalty(mid):
            high = mid
        else:
            low = mid + 1
    print(low)

