print("5722. 截断句子")

def truncateSentence(s, k):
    res = []
    start = 0
    n = len(s)
    for i in range(n):
        if s[i] == " ":
            t = s[start:i]
            start = i+1
            if len(t) > 0:
                res.append(t)
                if len(res) == k:
                    break
    if len(res) == k or start == n:
        return ' '.join(res)
    if start < n:
        res.append(s[start:])
        return ' '.join(res)


s = "Hello how are you Contestant"
k = 4
print(truncateSentence(s, k))
s = "Hello how are you"
print(truncateSentence(s, k))
s = "Hello how are"
print(truncateSentence(s, k))


print("\n5723. 查找用户活跃分钟数")

import collections
def findingUsersActiveMinutes(logs, k):
    dp = collections.defaultdict(set)
    for id, time in logs:
        dp[id].add(time)
    res = [0] * k
    for id, times in dp.items():
        res[len(times)-1] += 1
    return res



logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5
print(findingUsersActiveMinutes(logs, k))


print("\n 5724. 绝对差值和")

def minAbsoluteSumDiff(nums1, nums2):

    def micha(nums, target):
        left, right = 0, len(nums) - 1
        res = 10
        while left < right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                res = 0
                break
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

            if left == right:
                res = min(res, abs(target - nums[left]))
                if left == 0:
                    res = min(res, abs(target - nums[left + 1]))
                elif left == len(nums) - 1:
                    res = min(res, abs(target - nums[left - 1]))
                else:
                    res = min(res, abs(target - nums[left - 1]))
                    res = min(res, abs(target - nums[left + 1]))
        return res


    n = len(nums1)
    trueSum = 0
    dp = []
    for a, b in zip(nums1, nums2):
        t = abs(a-b)
        dp.append(t)
        trueSum += t

    if trueSum == 0:
        return 0

    anums = list(set(sorted(nums1)))
    min_v = 0
    for i in range(n):
        if dp[i] != 0:
            b = nums2[i]
            min_t = micha(anums, b)
            min_v = min(min_v, min_t - dp[i])
    return (trueSum + min_v) % (10 ** 9 + 7)







nums1 = [1,7,5]
nums2 = [2,3,5]
print(minAbsoluteSumDiff(nums1, nums2)) # 3

nums1 = [57,42,21,28,30,25,22,12,55,3,47,18,43,29,20,44,59,9,43,7,8,5,42,53,99,34,37,88,87,62,38,68,31,3,11,61,93,34,63,27,20,48,38,5,71,100,88,54,52,15,98,59,74,26,81,38,11,44,25,69,79,81,51,85,59,84,83,99,31,47,31,23,83,70,82,79,86,31,50,17,11,100,55,15,98,11,90,16,46,89,34,33,57,53,82,34,25,70,5,1]
nums2 = [76,3,5,29,18,53,55,79,30,33,87,3,56,93,40,80,9,91,71,38,35,78,32,58,77,41,63,5,21,67,21,84,52,80,65,38,62,99,80,13,59,94,21,61,43,82,29,97,31,24,95,52,90,92,37,26,65,89,90,32,27,3,42,47,93,25,14,5,39,85,89,7,74,38,12,46,40,25,51,2,19,8,21,62,58,29,32,77,62,9,74,98,10,55,25,62,48,48,24,21]
print(minAbsoluteSumDiff(nums1, nums2)) # 3441

nums1 = [1,10,4,4,2,7]
nums2 = [9,3,5,1,7,4]
print(minAbsoluteSumDiff(nums1, nums2)) # 20  8 7 1 3 5 3

nums1 = [56,51,39,1,12,14,58,82,18,41,70,64,18,7,44,90,55,23,11,79,59,76,67,92,60,80,57,11,66,32,76,73,35,65,55,37,38,26,4,7,64,84,98,61,78,1,80,33,5,66,32,30,52,29,41,2,21,83,30,35,21,30,13,26,36,93,81,41,98,23,20,19,45,52,25,51,52,24,2,45,21,97,11,92,28,37,58,29,5,18,98,94,86,65,88,8,75,12,9,66]
nums2 = [64,32,98,65,67,40,71,93,74,24,49,80,98,35,86,52,99,65,15,92,83,84,80,71,46,11,26,70,80,2,81,57,97,12,68,10,49,80,24,18,45,72,33,94,60,5,94,99,14,41,25,83,77,67,49,70,94,83,55,17,61,44,50,62,3,36,67,10,2,39,53,62,44,72,66,7,3,6,80,38,43,100,17,25,24,78,8,4,36,86,9,68,99,64,65,15,42,59,79,66]
print(minAbsoluteSumDiff(nums1, nums2)) # 3029


print("\n 二分查找")

def easySearch(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
print(easySearch([0,2,2,2,4], 4))
print(easySearch([0,2,2,2,4], 2))
print(easySearch([0,2,2,2,4], -1))
print(easySearch([0,2,2,2,4], 1))
print(easySearch([0,2,2,2,4], 5))

print("右侧二分查找")
def right_search(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left - 1
print(right_search([0,2,2,2,4], 4))
print(right_search([0,2,2,2,4], 2))
print(right_search([0,2,2,2,4], -1))
print(right_search([0,2,2,2,4], 1))
print(right_search([0,2,2,2,4], 5))

print("左侧二分查找")
def left_search(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid
        elif nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left
print(left_search([0,2,2,2,4], 4))
print(left_search([0,2,2,2,4], 2))
print(left_search([0,2,2,2,4], -1))
print(left_search([0,2,2,2,4], 1))
print(left_search([0,2,2,2,4], 5))

print("查找最小绝对差")

def minCha(nums, target):
    left, right = 0, len(nums)-1
    res = 10
    while left < right:
        mid = left + (right - left) // 2
        if target == nums[mid]:
            res = 0
            break
        if target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

        if left == right:
            res = min(res, abs(target - nums[left]))
            if left == 0:
                res = min(res, abs(target - nums[left+1]))
            elif left == len(nums) - 1:
                res = min(res, abs(target - nums[left-1]))
            else:
                res = min(res, abs(target - nums[left-1]))
                res = min(res, abs(target - nums[left+1]))
    return res



print(minCha([1,2,3,4,5,10], 7))
