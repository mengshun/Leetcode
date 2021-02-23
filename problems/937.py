"""
937. 重新排列日志文件
"""

def reorderLogFiles(logs):
    words = []
    nums = []
    dp = {}
    for v in logs:
        l = v.split(" ")
        last_str = list(l[-1])[-1]
        if 'a' <= last_str and last_str <= 'z':
            words.append(v)
            dp[v] = len(l[0])
        else:
            nums.append(v)
    words.sort(key= lambda x: x[:dp[x]])
    words.sort(key= lambda x: x[dp[x] + 1:])
    words.extend(nums)
    return words

def jiandanxiefa(logs):
    def dp(x):
        # 切割空格一次
        head, content = x.split(" ", 1)
        # 如果是 字符串内容 则先比较内容 在比较标题, 如果是数字, 则保持不变
        return (0, content, head) if content[0].isalpha() else (1, )
    return sorted(logs, key= dp)

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig", "let4 art zero","let3 art zero"]
print(reorderLogFiles(logs)) # ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
print(jiandanxiefa(logs))

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
print(reorderLogFiles(logs)) # ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
print(jiandanxiefa(logs))
