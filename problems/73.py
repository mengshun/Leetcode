"""
73. 矩阵置零
https://leetcode-cn.com/problems/set-matrix-zeroes/
"""

def setZeroes(matrix):
    if not matrix or not matrix[0]:
        return []
    m = len(matrix)
    n = len(matrix[0])
    dp = [False] * (m + n) # 第m行  第n + m 列
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                dp[i] = True
                dp[m + j] = True
    for i in range(m):
        for j in range(n):
            if dp[i] or dp[m + j]:
                matrix[i][j] = 0

def setZeroesOther(matrix):
    if not matrix or not matrix[0]:
        return []
    m = len(matrix)
    n = len(matrix[0])
    row_flag = any(matrix[0][i] == 0 for i in range(n))
    column_flag = any(matrix[i][0] == 0 for i in range(m))

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if row_flag:
        for i in range(n):
            matrix[0][i] = 0
    if column_flag:
        for i in range(m):
            matrix[i][0] = 0







matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)
print(matrix) # [[1,0,1],[0,0,0],[1,0,1]]

matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroesOther(matrix)
print(matrix) # [[1,0,1],[0,0,0],[1,0,1]]



print("============289 生命游戏===========")

def gameOfLife(board):
    copy_board = [[x for x in v] for v in board]
    m = len(copy_board)
    n = len(copy_board[0])
    def get_current_val(x, y):
        if x < 0 or y < 0 or x >= m or y >= n:
            return 0
        return copy_board[x][y]
    def get_sum_v(x, y):
        res = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                res += get_current_val(i, j)
        return res - copy_board[x][y]

    for i in range(m):
        for j in range(n):
            cur_sum = get_sum_v(i, j)
            if copy_board[i][j] == 1:
                if not (cur_sum == 2 or cur_sum == 3):
                    board[i][j] = 0
            else:
                if cur_sum == 3:
                    board[i][j] = 1


board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
gameOfLife(board)
print(board) # [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
