n, m = map(int, input().split())
col_chars = [[0 for _ in range(26)] for _ in range(m)]
row_chars = [[0 for _ in range(26)] for _ in range(n)]

mat = ["" for _ in range(n)]

for r in range(n):
    mat[r] = input()
    for c in range(m):
        pos = ord(mat[r][c]) - ord('a')  # 'z' - 'a' => 122 - 97 = 25
        col_chars[c][pos] += 1
        row_chars[r][pos] += 1

res = []

for r in range(n):
    for c in range(m):
        pos = ord(mat[r][c]) - ord('a')
        if col_chars[c][pos] == 1 and row_chars[r][pos] == 1:
            res.append(mat[r][c])

print("".join(res))

# def crossword(res, n, m):
#     seen_hash_r = {}
#     for row in range(n):
#         seen_r = set()
#         for col in range(m):
#             if res[row][col] in seen_r:
#                 seen_hash_r[res[row][col]] = [row, col]
#             else:
#                 seen_r.add(res[row][col])
    
#     seen_hash_c = {}
#     for col in range(m):
#         seen_c = set()
#         for row in range(n):
#             if res[row][col] in seen_c:
#                 seen_hash_c[res[row][col]] = [row, col]
#             else:
#                 seen_c.add(res[row][col])

    
#     # when I am done noting down duplicates and their positions,
#     # I cross them out in two loops

#     for key_r in seen_hash_r:
#         for col in range(m):
#             rdx = seen_hash_r[key_r][0]
#             if res[rdx][col] == key_r:
#                 res[rdx][col] = 0
    
#     for key_c in seen_hash_c:
#         for row in range(n):
#             cdx = seen_hash_c[key_c][1]
#             if res[row][cdx] == key_c:
#                 res[row][cdx] = 0
    
#     result = ''
#     for i in range(n):
#         for j in range(m):
#             if res[i][j] != 0:
#                 result += res[i][j]
    
#     return result 



# res = []
# n, m = map(int, input().split())
# for _ in range(n):
#     a = list(input().strip())
#     res.append(a)
# print(crossword(res, n, m))