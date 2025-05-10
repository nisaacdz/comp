digits = list(input())

if digits[0] == 9:
    print()

for i in range(1, len(digits)):
    digit_num = int(digits[i])
    digits[i] = str(min(digit_num, 9 - digit_num))

ans = "".join(digits).lstrip('0')

print(ans if len(ans) > 0 else 9)