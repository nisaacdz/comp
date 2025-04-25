n = int(input())
costs = sorted(map(int, input().split()), reverse=True)
m = int(input())
coupons = list(map(int, input().split()))

total = sum(costs)

for coupon in coupons:
    print(total - costs[coupon - 1])