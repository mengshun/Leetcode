"""
1006. 笨阶乘
https://leetcode-cn.com/problems/clumsy-factorial/
"""

def clumsy(N):
    res = float("inf")
    stack = []
    for v in range(N, 0, -1):
        stack.append(v)
        if len(stack) == 4:
            if res == float("inf"):
                res = int(stack[0] * stack[1] / stack[2] + stack[3])
            else:
                res -= int(stack[0] * stack[1] / stack[2] - stack[3])
            stack = []
    if N < 4:
        res = 0
    if len(stack) == 1:
        res -= stack[0]
    elif len(stack) == 2:
        res -= int(stack[0] * stack[1])
    elif len(stack) == 3:
        res -= int(stack[0] * stack[1] / stack[2])
    return res if N >= 4 else -res

def clumsyOther(N):
    op = 0 # * / + -
    stack = [N]
    for v in range(N-1, 0, -1):
        if op == 0:
            stack.append(stack.pop() * v)
        elif op == 1:
            stack.append(int(stack.pop() / float(v)))
        elif op == 2:
            stack.append(v)
        elif op == 3:
            stack.append(-v)
        op = (op+1) % 4
    return sum(stack)



print(clumsy(1)) # 1
print(clumsy(4)) # 7
print((clumsy(10))) # 12
print(clumsyOther(1)) # 1
print(clumsyOther(4)) # 7
print((clumsyOther(10))) # 12


print("282. 给表达式添加运算符")

def addOperators(num, target):
    res = []
    def check(s):
        stack = []
        op = 1
        num = 0
        for v in s:
            if v not in "+-*":
                num = num * 10 + int(v)
            else:
                if op < 2:
                    stack.append(num * op)
                else:
                    stack.append(stack.pop() * num)
                if v == "+":
                    op = 1
                elif v == "-":
                    op = -1
                elif v == "*":
                    op = 2
                num = 0
        if op < 2:
            stack.append(num * op)
        else:
            stack.append(stack.pop() * num)
        if sum(stack) == target:
            res.append(s)

    def backtrace(num_s, t):
        if not num_s:
            check(t + num_s)
            return
        if num_s[0] == "0":
            if len(num_s) == 1:
                backtrace(num_s[1:], t + num_s[0])
                backtrace(num_s[1:], t + num_s[0])
                backtrace(num_s[1:], t + num_s[0])
            else:
                backtrace(num_s[1:], t + num_s[0] + "+")
                backtrace(num_s[1:], t + num_s[0] + "-")
                backtrace(num_s[1:], t + num_s[0] + "*")
        else:
            n = len(num_s)
            for i in range(1, n+1):
                tmp = num_s[:i]
                other = num_s[i:]
                if i == n:
                    backtrace(other, t + tmp)
                else:
                    backtrace(other, t + tmp + "+")
                    backtrace(other, t + tmp + "-")
                    backtrace(other, t + tmp + "*")
    backtrace(num, "")
    return res

print(addOperators("123", 6))
print(addOperators("3456237490", 9191))
print(addOperators("105", 5)) # ["1*0+5","10-5"]