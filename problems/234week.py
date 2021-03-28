"""
234 周赛
"""

print("5713. 字符串中不同整数的数目")
def numDifferentIntegers(word):
    if not word:
        return None
    dpset = set()
    left = right = 0
    n = len(word)
    for i in range(n):
        cur = word[i]
        if cur <= "z" and cur >= "a":
            if right - left > 0:
                dpset.add(int(word[left:right]))
            left = i + 1
        right += 1
    if left != right:
        dpset.add(int(word[left:right]))
    return len(dpset)



print(numDifferentIntegers("a123bc34d8ef34")) #3
print(numDifferentIntegers("leet1234code234")) #2
print(numDifferentIntegers("a1b01c001")) #1


print("\n\n5715. 还原排列的最少操作步数")
def reinitializePermutation(n):
    perm = list(range(n))

    res = 0
    def dfs(t):
        nonlocal res
        res += 1
        t = [x for x in t]
        queue = []
        for i in range(n):
            cur = t[i // 2] if i % 2 == 0 else t[n//2 + (i-1) // 2]
            perm[i] = cur
            if i == 0:
                queue.append(cur)
            elif len(queue) == i:
                if queue[-1] < cur:
                    queue.append(cur)
        if len(queue) != n:
            dfs(perm)
    dfs(perm)
    return res




print(reinitializePermutation(6)) # 6


print("\n\n5714. 替换字符串中的括号内容")

def evaluate(s, knowledge):
    key_words = {key:value for key, value in knowledge}
    n = len(s)
    left = right = None
    res = ""
    for i in range(n):
        if s[i] == "(":
            left = i + 1
        elif s[i] == ")":
            right = i
            key = s[left:right]
            if key in key_words:
                res += key_words[key]
            else:
                res += "?"
            left = None
        elif left == None:
            res += s[i]

    return res





s = "(name)is(age)yearsold"
knowledge = [["name","bob"],["age","two"]]
print(evaluate(s, knowledge))

s = "hi(name)"
knowledge = [["a","b"]]
print(evaluate(s, knowledge))

s = "(a)(a)(a)aaa"
knowledge = [["a","yes"]]
print(evaluate(s, knowledge))

s = "(a)(b)"
knowledge = [["a","b"],["b","a"]]
print(evaluate(s, knowledge))


print("\n\n 5716. 好因子的最大数目")
import math
# 会超时
def maxNiceDivisors(primeFactors):
    dp = [x for x in range(primeFactors + 1)]
    for i in range(2, primeFactors + 1):
        for j in range(i):
            dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
    return dp[primeFactors] % (10**9 + 7)


print(maxNiceDivisors(5)) # 6
print(maxNiceDivisors(8)) # 18
print(maxNiceDivisors(18)) # 729

def maxNiceDivisorsOther(primeFactors):
    # t = (primeFactors - 2) // 3
    # return (primeFactors - 3 * max(0, t)) * pow(3, int(max(0, t)), 10 ** 9 + 7) % (10 ** 9 + 7)

    if primeFactors <= 4:
        return primeFactors
    # primeFactors = 3a + b
    a, b = primeFactors // 3, primeFactors % 3
    res = 0
    K = 10 ** 9 + 7
    if b == 0:
        res = pow(3, a, K)
    elif b == 2:
        res = (pow(3, a, K) * 2) % K
    elif b == 1:
        res = (pow(3, a-1, K) * 4) % K
    return res

print(maxNiceDivisorsOther(3)) # 6
print(maxNiceDivisorsOther(4)) # 6
print(maxNiceDivisorsOther(5)) # 6
print(maxNiceDivisorsOther(6)) # 6
print(maxNiceDivisorsOther(7)) # 6
print(maxNiceDivisorsOther(8)) # 18
print(maxNiceDivisorsOther(18)) # 18
print(maxNiceDivisorsOther(545918790)) # 421090465





def zhishu(n):
    dp = [2]
    for i in range(3, n+1, 2):
        x = int(math.sqrt(i))
        dp.append(i)
        for j in range(2, x+1):
            if i % j == 0:
                dp.pop()
                break
    return dp

print(zhishu(100))