"""
54. 螺旋矩阵
https://leetcode-cn.com/problems/spiral-matrix/
"""

def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []
    rows, columns = len(matrix), len(matrix[0])
    res = []
    left, right, top, bottom = 0, columns-1, 0, rows-1
    while left <= right and top <= bottom:
        for column in range(left, right+1):
            res.append(matrix[top][column])
        for row in range(top+1, bottom+1):
            res.append(matrix[row][right])
        if left < right and top < bottom:
            for column in range(right-1, left, -1):
                res.append(matrix[bottom][column])
            for row in range(bottom, top, -1):
                res.append(matrix[row][left])
        top, left, bottom, right = top+1, left+1, bottom-1, right-1
    return res


def spiralOrderOther(matrix):
    if not matrix or not matrix[0]:
        return []
    m, n = len(matrix), len(matrix[0])
    size = m * n
    res = []
    left, right, top, bottom = 0, n-1, 0, m-1
    direction = 1 # 1 右 2 下 3 左 4 上
    x, y = 0, 0
    while len(res) != size:
        res.append(matrix[x][y])
        if direction == 1:
            if y < right:
                y += 1
            else:
                direction = 2
                x += 1
                top += 1
        elif direction == 2:
            if x < bottom:
                x += 1
            else:
                direction = 3
                y -= 1
                right -= 1
        elif direction == 3:
            if y > left:
                y -= 1
            else:
                direction = 4
                x -= 1
                bottom -= 1
        elif direction == 4:
            if x > top:
                x -= 1
            else:
                direction = 1
                y += 1
                left += 1
    return res





print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,3,6,9,8,7,4,5]
print(spiralOrderOther([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,3,6,9,8,7,4,5]
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])) # [1,2,3,4,8,12,11,10,9,5,6,7]
print(spiralOrderOther([[1,2,3,4],[5,6,7,8],[9,10,11,12]])) # [1,2,3,4,8,12,11,10,9,5,6,7]

"""
59. 螺旋矩阵II
https://leetcode-cn.com/problems/spiral-matrix-ii/
"""

def generateMatrix(n):

    res = [[1] * n for _ in range(n)]

    top, left, bottom, right = 0, 0, n-1, n-1
    t = 0
    while top <= bottom and left <= right:
        for y in range(left, right+1):
            t += 1
            res[top][y] = t
        for x in range(top+1, bottom):
            t += 1
            res[x][right] = t
        for y in range(right, left, -1):
            t += 1
            res[bottom][y] = t
        for x in range(bottom, top, -1):
            t += 1
            res[x][left] = t
        top, left, bottom, right = top+1, left+1, bottom - 1, right - 1

    return res







print(generateMatrix(3))
print(generateMatrix(1))
