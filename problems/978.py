"""
978. 最长湍流子数组
https://leetcode-cn.com/problems/longest-turbulent-subarray/
"""

# 首次尝试
def maxTurbulenceSize(arr):
    n = len(arr)
    if n < 2:
        return n

    max_count = count = 1
    increase = True
    for i in range(1, n):
        if arr[i] == arr[i-1]:
            count = 1
        elif count == 1:
            increase = arr[i] > arr[i-1]
            count += 1
        elif increase and arr[i] < arr[i-1]:
            count += 1
            increase = False
        elif not increase and arr[i] > arr[i-1]:
            count += 1
            increase = True
        else:
            count = 2
            increase = arr[i] > arr[i-1]
        max_count = max(max_count, count)
    return max_count

# 双指针
def zhizhen(arr):
    n = len(arr)
    ret = 1
    left = right = 0
    while right < n-1:
        if left == right:
            if arr[left] == arr[left+1]:
                left += 1
            right += 1
        else:
            if arr[right-1] < arr[right] and arr[right] > arr[right+1]:
                right += 1
            elif arr[right-1] > arr[right] and arr[right] < arr[right+1]:
                right += 1
            else:
                left = right
        ret = max(ret, right - left + 1)
    return ret


# 动态规划
def dp_function(arr):
    n = len(arr)
    # [1, 1] 分别代表 递增 递减 子数组个数
    dp = [[1, 1] for _ in range(n)]
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            dp[i][0] = dp[i-1][1] + 1
        elif arr[i] < arr[i-1]:
            dp[i][1] = dp[i-1][0] + 1
    res = 1
    for x, y in dp:
        res = max(res, x, y)
    return res



print(maxTurbulenceSize([9,4,2,10,7,8,8,1,9])) # 5
print(zhizhen([9,4,2,10,7,8,8,1,9]))
print(dp_function([9,4,2,10,7,8,8,1,9]))