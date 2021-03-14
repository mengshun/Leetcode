"""
705. 设计哈希集合
https://leetcode-cn.com/problems/design-hashset/
"""

class HashNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.base = 769
        self.data = [HashNode(0) for _ in range(self.base)]

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        head = self.data[key % self.base]
        cur = HashNode(key)
        cur.next = head.next
        head.next = cur

    def remove(self, key: int) -> None:
        head = self.data[key % self.base]
        pre = head
        while head.next:
            cur = head.next
            if cur.val == key:
                pre.next = cur.next
                break
            pre = cur

    def contains(self, key: int) -> bool:
        head = self.data[key % self.base]
        while head.next:
            if head.next.val == key:
                return True
            head = head.next
        return False


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.add(2)
obj.add(3)
obj.add(4)
obj.add(5)
print(obj.contains(5))
print(obj.contains(4))
obj.remove(4)
print(obj.contains(4))


class MyHashSetOther:

    def __init__(self):
        self.hashSet = {}

    def add(self, key: int) -> None:
        self.hashSet[key] = 1

    def remove(self, key: int) -> None:
        if key in self.hashSet:
            self.hashSet.pop(key)

    def contains(self, key: int) -> bool:
        return key in self.hashSet


class MyHashSetWuDe:

    def __init__(self):
        self.data = [False] * 1000001

    def add(self, key: int) -> None:
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key]






def areAlmostEqual(s1, s2):
    dp = []
    for x, y in zip(s1, s2):
        if x != y:
            dp.append((x, y))
            if len(dp) > 2:
                return False
    if len(dp) == 0:
        return True
    if len(dp) == 2:
        x1, y1 = dp[0]
        x2, y2 = dp[1]
        return x1 == y2 and y1 == x2
    return False



print("areAlmostEqual", areAlmostEqual("bank", "kanb"))
s1 = "ab"
s2 = "ba"
print("areAlmostEqual", areAlmostEqual(s1, s2))



def findCenter(edges):
    x, y = edges[0], edges[1]
    for v in x:
        if v in y:
            return v
    return 0

edges = [[1,2],[5,1],[1,3],[1,4]]
print(findCenter(edges))

#好子数组的最大分数
def maximumScore(nums, k):

    res = 0
    n = len(nums)
    left, right = k, k
    min_v = nums[k]
    while 1:
        while left >= 0 and nums[left] >= min_v:
            left -= 1
        while right < n and nums[right] >= min_v:
            right += 1
        res = max(res, min_v * (right - left - 1))
        if left >= 0 and right < n:
            min_v = max(nums[left], nums[right])
        if left < 0 and right == n:
            break
        elif left < 0:
            min_v = nums[right]
        elif right == n:
            min_v = nums[left]
    return res

nums = [1,4,3,7,4,5]
k = 3
print("maximumScore", maximumScore(nums, k))
nums = [6569,9667,3148,7698,1622,2194,793,9041,1670,1872]
k = 5
print("maximumScore", maximumScore(nums, k)) # 9732
nums = [1,4,3,7,4,5]
k = 3
print("maximumScore", maximumScore(nums, k)) # 9732