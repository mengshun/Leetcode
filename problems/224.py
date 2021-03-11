"""
224. 基本计算器
https://leetcode-cn.com/problems/basic-calculator/
"""

def calculate(s: str):
    ops = [1]
    sign = 1
    res = 0
    n = len(s)
    i = 0
    while i < n:
        if s[i] == " ":
            i += 1
        elif s[i] == "+":
            sign = ops[-1]
            i += 1
        elif s[i] == "-":
            sign = -ops[-1]
            i += 1
        elif s[i] == "(":
            ops.append(sign)
            i += 1
        elif s[i] == ")":
            ops.pop()
            i += 1
        else:
            num = 0
            while i < n and s[i] >= "0" and s[i] <= "9":
                num = num * 10 + int(s[i])
                i += 1
            res += sign * num
    return res



def myFunction(s: str):
    res, num, sign = 0, 0, 1
    stack = []
    for c in s:
        if c.isnumeric():
            num = 10 * num + int(c)
        elif c == "+" or c == "-":
            res += sign * num
            num = 0
            sign = 1 if c == "+" else -1
        elif c == "(":
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif c == ")":
            res += sign * num
            num = 0
            res *= stack.pop()
            res += stack.pop()
    res += sign * num
    return res

print(calculate("1 + (1123 - (2 + 3) - 5)"))
print(myFunction("1 + (1123 - (2 + 3) - 5)"))




def my(s: str):
    res, sign, num = 0, 1, 0
    stack = []
    for c in s:
        if c.isnumeric():
            num = num * 10 + int(c)
        elif c == "+" or c == "-":
            res += sign * num
            num = 0
            sign = 1 if c == "+" else -1
        elif c == "(":
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif c == ")":
            res += sign * num
            res *= stack.pop()
            res += stack.pop()
            num = 0
    res += sign * num
    return res


print(my("1 + (1123 - (2 + 3) - 5)"))


"""
227. 基本计算器  II
https://leetcode-cn.com/problems/basic-calculator-ii/
"""

def calcuatetwo(s: str):

    stack = []
    pre_op = "+"
    num = 0
    n = len(s)
    for i, c in enumerate(s):
        if c.isnumeric():
            num = num * 10 + int(c)
        if c in "+-*/" or i == n -1:
            if pre_op == "+":
                stack.append(num)
            elif pre_op =="-":
                stack.append(-num)
            elif pre_op == "*":
                stack.append(stack.pop() * num)
            elif pre_op == "/":
                top = stack.pop()
                if top < 0:
                    stack.append(int(top / num))
                else:
                    stack.append(top // num)
            num = 0
            pre_op = c
    return sum(stack)




print(calcuatetwo("3 + 5 / 5 + 2"))
print(calcuatetwo("14 - 3 / 2 + 5 - 6 / 4"))








