"""
1774. 最接近目标价格的甜点成本
https://leetcode-cn.com/problems/closest-dessert-cost/
"""

def closestCost(baseCosts, toppingCosts, target):
    # baseCosts = sorted(baseCosts)
    # toppingCosts = sorted(toppingCosts)

    res = float('inf')
    def deal(v):
        nonlocal res
        if abs(v - target) < abs(res - target) or (abs(v - target) == abs(res - target) and v < res):
            res = v
            print(v)
        return res == target

    n = len(toppingCosts)
    for base in baseCosts:
        if deal(base):
            return target
        for i in range(n):
            if deal(toppingCosts[i] + base) or deal(2 * toppingCosts[i] + base):
                return target
            for j in range(i+1, n):
                if deal(toppingCosts[i] + toppingCosts[j] + base) or deal(toppingCosts[i] + 2 * toppingCosts[j] + base):
                    return target
                if deal(2 * toppingCosts[i] + toppingCosts[j] + base) or deal(2 * toppingCosts[i] + 2 * toppingCosts[j] + base):
                    return target
    return res if res != float('inf') else 0

# print(closestCost([1, 7], [3, 4], 10)) # 10
# print(closestCost([2, 3], [4, 5, 100], 18)) # 17
# print(closestCost([3], [5, 2], 9)) # 8
print(closestCost([4152,7816,5153,1641,3402,5201], [650,447,173,4843], 9775)) # 9788
print(closestCost([4152,7816,5153,1641,3402,5201], [650,447,173,4843], 9775)) # 9788


def countHomogenous(s):
    n = len(s)
    left, right, count = 0, 0, 0
    k = 10 ** 9 + 7
    while right < n:
        if s[left] != s[right]:
            left = right
        else:
            count = (count + right - left + 1) % k
            right += 1
    return count

print(countHomogenous("abbcccaa"))


