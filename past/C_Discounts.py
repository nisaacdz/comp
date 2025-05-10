n = int(input())
costs = sorted(map(int, input().split()), reverse=True)
m = int(input())
cc = list(map(int, input().split()))

cc_sum = sum(costs)

for coupon in cc:
    print(cc_sum - costs[coupon - 1])