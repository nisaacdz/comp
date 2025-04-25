n = int(input())
gifts = [0 for _ in range(n)]
gg = list(map(int, input().split()))
for i in range(n):
    v = gg[i]
    gifts[v - 1] = i + 1

print(" ".join(map(str, gifts)))