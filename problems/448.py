"""
448. 找到所有数组中消失的数字
"""

def findDisappearedNumbers(nums):
    n = len(nums)
    for v in nums:
        t = (v - 1) % n
        nums[t] += n
    res = [x+1 for x in range(n) if nums[x] <= n]
    return res

print(findDisappearedNumbers([4,3,2,7,8,2,3,1])) # [5, 6]


"""
442. 数组中重复的数据
"""

def findDuplicates(nums):
    n = len(nums)
    for v in nums:
        nums[(v - 1) % n] += n
    return [x+1 for x in range(n) if nums[x] > 2*n]
def other(nums):
    res = []
    for v in nums:
        t = int(abs(v))
        if nums[t - 1] < 0:
            res.append(t)
        else:
            nums[t - 1] *= -1
    return res





print(findDuplicates([4,3,2,7,8,2,3,1])) # [2, 3]
print(other([4,3,2,7,8,2,3,1])) # [2, 3]

