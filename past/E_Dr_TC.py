t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    ones = sum(map(int, s))
    zeros = n - ones

    ans = (n * ones) + zeros - ones

    print(ans)
