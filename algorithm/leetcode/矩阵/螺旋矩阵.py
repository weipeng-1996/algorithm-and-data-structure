# 54
# 模拟路径
def spiralOrder(matrix):
    if not matrix: return []
    R, C = len(matrix), len(matrix[0])
    seen = [[False] * C for _ in range(R)]
    arr = []
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r = c = d = 0
    for _ in range(R * C):
        arr.append(matrix[r][c])
        seen[r][c] = True
        tr, tc = r + dr[d], c + dc[d]
        if -1 < tr < R and -1 < tc < C and seen[tr][tc] == False:
            r, c = tr, tc
        else:
            d = (d + 1) % 4
            r, c = r + dr[d], c + dc[d]
    return arr

# 按层模拟


def spiralOrder1(matrix):
    def spiral(r1, r2, c1, c2):
        for c in range(c1, c2 + 1):
            yield r1,c
        for r in range(r1 + 1, r2 + 1):
            yield r, c2
        if r1 < r2 and c1 < c2:
            for c in range(c2 - 1, c1, -1):
                yield r2, c
            for r in range(r2, r1, -1):
                yield r, c1
    if not matrix: return []
    r1, r2 = 0, len(matrix) - 1
    c1, c2 = 0, len(matrix[0]) - 1
    ans = []
    while r1 <= r2 and c1 <= c2:
        for r, c in spiral(r1, r2, c1, c2):
            ans.append(matrix[r][c])
        r1 += 1
        r2 -= 1
        c1 += 1
        c2 -= 1
    return ans


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(spiralOrder1(matrix))

