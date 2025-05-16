n, k = map(int, input().split())

theorems = list(map(int, input().split()))

sleepiness = list(map(int, input().split()))

wrote = sum((0 if s == 0 else t) for (t, s) in zip(theorems, sleepiness))

maxCoverable = sum((0 if s else t) for (t, s) in zip(theorems[:k], sleepiness[:k]))

current = maxCoverable

for c in range(k, n):
    current -= theorems[c - k] if sleepiness[c - k] == 0 else 0
    current += theorems[c] if sleepiness[c] == 0 else 0

    maxCoverable = max(maxCoverable, current)
    
print(wrote + maxCoverable)