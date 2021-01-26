"""
69. x 的平方根
"""

def mySqrt(x):
    if x < 2:
        return x
    start = 1
    end = x >> 1
    while end > start:
        mid = start + (end - start >> 1)
        res = mid * mid
        if res == x:
            return mid
        elif res > x:
            end = mid - 1
        else:
            start = mid + 1
    return start if start * start <= x else (start - 1)


print(mySqrt(4))
print(mySqrt(8))