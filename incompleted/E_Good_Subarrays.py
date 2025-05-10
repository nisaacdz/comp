from collections import defaultdict

"""
We need to know how many subarrays have a sum equal to their lengths
in better than O(n^2) time
Each number is in range [0, 9]
They l3
"""

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    value_dict = defaultdict(int)
    value_dict[1] = 1

    cur_sum, ans = 0, 0

    for i in range(n):
        cur_sum += int(s[i])
        ans += value_dict[cur_sum - i]
        value_dict[cur_sum - i] += 1
    
    print(ans)
