t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    rems = {}

    for num in nums:
        if (k - num % k) % k == 0:
            continue
        if not rems.get((k - num % k) % k):
            rems[(k - num % k) % k] = 1
        else:
            rems[(k - num % k) % k] = rems.get((k - num % k) % k) + 1
    moves = 0
    rounds = 0
    for k, v in rems.items():
        rounds = max(rounds, v)
    rounds = rounds - 1
    ending = 0
    for k, v in rems.items():
        res = v - rounds
        if res > 0:
            ending = k
    ans = rounds * k + ending + 1
    print(ans)