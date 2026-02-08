t = int(input())

def solve(t: int):
    n = int(input())
    nums = list(map(int, input().split()))
    ans = n + len(nums)
    print(ans)

for t in range(t):
    solve(t)
