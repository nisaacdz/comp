s1 = input()
s2 = input()

mega_dict1 = []
mega_dict2 = []

cur_dict1 = [0 for _ in range(26)]
cur_dict2 = [0 for _ in range(26)]

for i in range(len(s1)):
    cur_dict1[ord(s1[i]) - ord('a')] += 1
    mega_dict1.append(cur_dict1.copy())

for i in range(len(s2)):
    cur_dict2[ord(s2[i]) - ord('a')] += 1
    mega_dict2.append(cur_dict2.copy())

def is_equivalent(l1, r1, l2, r2):
    size = r1 - l1 + 1
    diff1 = [0 for _ in range(26)]
    diff2 = [0 for _ in range(26)]

    for i in range(26):
        diff1[i] = mega_dict1[r1][i] - (mega_dict1[l1 - 1][i] if l1 > 0 else 0)
    for i in range(26):
        diff2[i] = mega_dict2[r2][i] - (mega_dict2[l2 - 1][i] if l2 > 0 else 0)
    
    if any(diff1[i] != diff2[i] for i in range(26)):
        # print("l1, r1, l2, r2 = ", l1, r1, l2, r2)
        # print("diffs aren't equal")
        # print(diff1)
        # print(diff2)
        return False
    # print("substrs check", size)
    # print(s1[l1:(r1 + 1)])
    # print(s2[l2:(r2 + 1)])
    
    if size % 2 == 1:
        return all(s1[l1 + k] == s2[l2 + k] for k in range(size))
    
    m1 = l1 - 1 + size // 2
    m2 = l2 - 1 + size // 2
    
    return (is_equivalent(l1, m1, l2, m2) and is_equivalent(m1 + 1, r1, m2 + 1, r2)) or (is_equivalent(l1, m1, m2 + 1, r2) and is_equivalent(m1 + 1, r1, l2, m2))

res = is_equivalent(0, len(s1) - 1, 0, len(s2) - 1)

print('YES' if res else 'NO')