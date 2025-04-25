k, n, w = map(int, input().split())

# a, 2a, 3a, ..., wa
# sum = k*w(w + 1) / 2

total = k * w * (w + 1) // 2

needed = max(total - n, 0)

print(needed)