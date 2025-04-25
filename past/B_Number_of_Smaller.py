n, m = map(int, input().split())

nums1 = input().split()
nums2 = input().split()

res = [0 for _ in range(m)]
idx1 = 0

for idx2 in range(m):
    while idx1 < n and int(nums1[idx1]) < int(nums2[idx2]):
        idx1 += 1
    res[idx2] = idx1

print(" ".join(map(str, res)))