n = int(input())

nums = list(map(int, input().split()))

left, right = 0, n - 1
sum_left, sum_right = 0, 0

alice_ate = 0
bob_ate = 0

while left <= right:
    if sum_left > sum_right:
        sum_right += nums[right]
        right -= 1
        bob_ate += 1
    else:
        sum_left += nums[left]
        left += 1
        alice_ate += 1

print(alice_ate, bob_ate)