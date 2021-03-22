"""
15. 三数之和
"""

# 会超时
def threeSum(nums):
    n = len(nums)
    if n < 3:
        return []
    res = {}
    t = sorted(nums)
    for i in range(n-2):
        for j in range(i+1, n-1):
            val = 0 - t[i] - t[j]
            if val in t[j+1:]:
                # 哈希会自动去重
                res[(t[i], t[j])] = val
    return [list(k) + [v] for k, v in res.items()]


def treeSumOther(nums):
    res = {}
    n = len(nums)
    nums = sorted(nums)
    for i in range(n-2):
        left, right = i+1, n-1
        while left < right:
            r = nums[i] + nums[left] + nums[right]
            if r == 0:
                res[(nums[i], nums[left])] = nums[right]
                left += 1
                right -= 1
            elif r < 0:
                t = left + 1
                while t < right and nums[t] == nums[left]:
                    t += 1
                left = t
            else:
                t = right - 1
                while t > left and nums[t] == nums[right]:
                    t -= 1
                right = t
    return [list(k) + [v] for k, v in res.items()]


def hashSumThree(nums):
    n = len(nums)
    if n < 3:
        return []
    nums = sorted(nums)
    dp = {}
    res = []
    for i in range(n):
        dp[nums[i]] = i

    for i in range(n-2):
        target = -nums[i]
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, n-1):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            t = target - nums[j]
            if t in dp and dp[t] > j:
                res.append([nums[i], nums[j], t])
    return res



nums = [-1,0,1,2,-1,-4] # -4 -1 -1 0 1 2
print(threeSum(nums))# [[-1,-1,2],[-1,0,1]]
print(treeSumOther(nums))# [[-1,-1,2],[-1,0,1]]
print(hashSumThree(nums))# [[-1,-1,2],[-1,0,1]]
nums = [-2,0,1,1,2]
print(treeSumOther(nums)) # [[-2, 0, 2], [-2, 1, 1]]
nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6] # [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
print(treeSumOther(nums))
print(hashSumThree(nums))
"""
16. 最接近的三数之和
"""

def threeSumClosest(nums, target):
    res = float('inf')
    def update(d):
        nonlocal res
        if abs(target - d) < abs(target - res):
            res = d
    nums.sort()
    n = len(nums)
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, n-1
        while left < right:
            r = nums[i] + nums[left] + nums[right]
            if r == target:
                return target
            update(r)
            if r > target:
                # 右 左移
                t = right - 1
                while left < t and nums[right] == nums[t]:
                    t -= 1
                right = t
            else:
                # 右移
                t = left + 1
                while right > t and nums[left] == nums[t]:
                    t += 1
                left = t
    return res

nums = [-1,2,1,-4] # -4 -1 1 2
target = 1
print(threeSumClosest(nums, target))
