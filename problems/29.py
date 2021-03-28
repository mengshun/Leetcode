"""
29. 两数相除
https://leetcode-cn.com/problems/divide-two-integers/
1. 如果被除数是0 则直接返回0
2. 先对结果的 符号 进行判定, 然后将被除数和除数 全部取正数
3. 由于不能用除法和乘法, 所以准备一个哈希 来存 除数的倍数, 例如 10/3, 哈希存储 {6:2, 3:1}
4. 对哈希的 倍数除数进行排序, 期望先取到最大的
5. 使用DFS 更新结果, 在循环时只要存在除数有效时 直接跳出循环
6. 对临界条件进行判定
"""

def divide(dividend, divisor):
    if dividend == 0:
        return 0
    is_minus = False
    if (divisor > 0 and dividend < 0) or (divisor < 0 and dividend > 0):
        is_minus = True
    dividend = int(abs(dividend))
    divisor = int(abs(divisor))
    dp = {divisor : 1}
    sum_v = divisor
    while sum_v + sum_v <= dividend:
        count = dp[sum_v]
        sum_v += sum_v
        dp[sum_v] = count + count
    keys = sorted(dp.keys(), reverse=True)
    res = 0
    def dfs(t):
        nonlocal res
        if t < divisor:
            return
        for v in keys:
            if t - v >= 0:
                res += dp[v]
                dfs(t - v)
                break
    dfs(dividend)
    if is_minus:
        res = -res
    if res >= -2 ** 31 and res <= 2 ** 31 - 1:
        return res
    return 2 ** 31 - 1




print(divide(10, 3))
print(divide(7, -3))
print(divide(-2147483648, -1)) # 2147483647