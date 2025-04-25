n, m = map(int, input().split())

nums1 = input().split()
nums2 = input().split()

idx1, idx2 = 0, 0

res = []

while idx1 < n and idx2 < m:
    if int(nums1[idx1]) < int(nums2[idx2]):
        res.append(nums1[idx1])
        idx1 += 1
    else:
        res.append(nums2[idx2])
        idx2 += 1

res.extend(nums1[idx1:])
res.extend(nums2[idx2:])

print(" ".join(res))