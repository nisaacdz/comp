t = int(input())

for _ in range(t):
    n = int(input())
    a = map(int, input().split())

    states = [1, 0, 0, 0]
    for num in a:
        if num == 2:
            states[num] = 2 * states[num] % 998244353
        states[num] = (states[num] + states[num - 1]) % 998244353
        
    print(states[3])
