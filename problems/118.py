"""
118 杨辉三角
"""

def generate(numRows):

    res = []
    for i in range(numRows):
        t = []
        for j in range(i + 1):
            if j == 0 or j == i:
                t.append(1)
            else:
                t.append(res[i-1][j-1] + res[i-1][j])
        res.append(t)
    return res


res = generate(5)
for v in res:
    print(v)