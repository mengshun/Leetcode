"""
35. 搜索插入位置
"""

def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)

def searchInsert2(nums, target):
    n = len(nums)
    left, right, ans = 0, n-1, n
    while left <= right:
        mid = ((right - left) >> 1) + left
        if target <= nums[mid]:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans




print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))
print(searchInsert([1,3,5,6], 0))

print(searchInsert2([1,3,5,6], 5))
print(searchInsert2([1,3,5,6], 2))
print(searchInsert2([1,3,5,6], 7))
print(searchInsert2([1,3,5,6], 0))



def countAndSay(n):
    res = "1"
    if n == 1:
        return res

    for i in range(n-1):
        dp = []
        tmp = ""
        for v in res:
            if len(dp) == 0 or v in dp:
                pass
            else:
                tmp += "{}{}".format(len(dp), dp[0])
                dp = []
            dp.append(v)

        if len(dp) > 0:
            tmp += "{}{}".format(len(dp), dp[0])
        res = tmp
    return res


# https://leetcode-cn.com/problems/count-and-say/solution/38-wai-guan-shu-lie-shuang-zhi-zhen-by-yiluolion/

#双指针思路
def say(n):
    if n == 1:
        return "1"
    say = ["1"]
    for _ in range(n-1):
        pre = say[0]
        count = 1
        cur_say = []
        for c in say[1:]:
            if c == pre:
                count += 1
            else:
                cur_say.extend([str(count), pre])
                pre = c
                count = 1
        cur_say.extend([str(count), pre])
        say = cur_say
    return "".join(say)


def say2(n):
    pre = ''
    cur = "1"
    for _ in range(n-1):
        pre = cur
        cur = ""
        start = end = 0
        while end < len(pre):
            while end < len(pre) and pre[start] == pre[end]:
                end += 1
            cur += str(end - start) + pre[start]
            start = end
    return cur


print("==============")
print(countAndSay(1))
print(say(1))
print(countAndSay(2))
print(say(2))
print(countAndSay(3))
print(say(3))
print(countAndSay(14))
print(say(14))
print(say2(14))