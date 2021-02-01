"""
888. 公平的糖果棒交换
"""

def fairCandySwap(A, B):
    sumA = sum(A)
    sumB = sum(B)
    # val = a - b
    val = (sumA - sumB) // 2
    # 转换为集合模式 检索更加快 查找效率：set>dict>list
    res = set(A)
    for b in B:
        a = val + b
        if a in res:
            return [a, b]
    return []

print(fairCandySwap([1, 1], [2, 2]))

"""
数学思维:
sumA - a + b = sumB - b + a
sumA - sumB = 2 (a - b)
a = (sumA - sumB)/2 + b
将A转换为集合模式 检索更加快 查找效率：set>dict>list
"""