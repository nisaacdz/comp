t = int(input())

for _ in range(t):
    a = int(input())
    numsA = list(map(int, input().split()))
    b = int(input())
    numsB = list(map(int, input().split()))

    maxSumA = numsA[0]
    maxSumB = numsB[0]

    for i in range(1, a):
        numsA[i] += numsA[i - 1]
        maxSumA = max(maxSumA, numsA[i])
    
    for j in range(1, b):
        numsB[j] += numsB[j - 1]
        maxSumB = max(maxSumB, numsB[j])
    
    print(max(0, maxSumA) + max(0, maxSumB))