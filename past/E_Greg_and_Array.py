n, m, k = map(int, input().split())

nums = list(map(int, input().split()))
state = [0 for _ in range(n + 1)]
operations = []

for _ in range(m):
    l, r, d = map(int, input().split())
    operations.append((l - 1, r - 1, d))

apply = [0 for _ in range(m + 1)]

for _ in range(k):
    x, y = map(int, input().split())
    apply[x - 1] += 1
    apply[y] -= 1

for i in range(1, m + 1):
    apply[i] += apply[i - 1]

for i in range(m):
    l, r, d = operations[i]
    state[l] += d * apply[i]
    state[r + 1] -= d * apply[i]

for i in range(1, n + 1):
    state[i] += state[i - 1]

for i in range(n):
    nums[i] += state[i]

print(*nums)