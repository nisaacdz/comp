t = int(input())

for _ in range(t):
    n = int(input())
    weights = list(map(int, input().split()))

    left, right = 0, n - 1
    ate_left, ate_right = 0, 0

    max_equal = 0

    while left <= right:
        if ate_left >= ate_right:
            ate_right += weights[right]
            right -= 1
        else:
            ate_left += weights[left]
            left += 1
        if ate_left == ate_right:
            max_equal = left + (n - right - 1)

    print(max_equal)