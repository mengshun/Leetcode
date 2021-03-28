"""
150. 逆波兰表达式求值
https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/
"""

def evalRPN(tokens):
    queue = []
    for v in tokens:
        if v in "+-*/":
            b = queue.pop()
            a = queue.pop()
            res = 0
            if v == "+":
                res = a + b
            elif v == "-":
                res = a - b
            elif v == "*":
                res = a * b
            else:
                if a * b < 0:
                    res = - (-a // b)
                else:
                    res = a // b
            queue.append(res)
        else:
            queue.append(int(v))
    return queue[-1]



print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])) # 22
