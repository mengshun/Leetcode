"""
6. Z 字形变换
"""

def convert(s, numRows):
    if numRows < 2:
        return s
    count = 0
    add_flag = False
    res = [[] for _ in range(numRows)]
    for v in s:
        res[count].append(v)
        if count == numRows - 1 or count == 0:
            add_flag = not add_flag
        if add_flag:
            count += 1
        else:
            count -= 1
    ret = ""
    for l in res:
        ret += "".join(l)
    return ret


print(convert("PAYPALISHIRING", 3)) # "PAHNAPLSIIGYIR"


"""
8. 字符串转换整数 (atoi)
"""

import re
def myAtoi(s):

    # reg = r"^[\+\-]?\d+"
    # res = re.findall(reg, s.lstrip())
    # print(res, int(*res))
    return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2 ** 31 - 1), -2 ** 31)

    start = right = 0
    has_find = False
    for i in range(len(s)):
        if has_find:
            if s[i] == " " or s[i].isalpha() or s[i] == ".":
                break
        else:
            if s[i] == "+" or s[i] == "-" or s[i].isnumeric():
                start = i
                has_find = True
            elif s[i].isalpha() or s[i] == ".":
                return 0
        right += 1

    if not has_find or start == right:
        return 0
    res = s[start:right]
    ret = int(res)
    if ret < (- 1 << 31):
        return - 1 << 31
    if ret > ((1 << 31) - 1):
        return (1 << 31) - 1
    return ret

print(myAtoi("42"))
print(myAtoi("  -42"))
print(myAtoi("4193 with words"))
print(myAtoi("words and 987"))
print(myAtoi("-91283472332"))
print(myAtoi("-3.154"))
print(myAtoi(".1"))