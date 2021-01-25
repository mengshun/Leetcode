"""
721. 账户合并
给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，其余元素是 emails 表示该账户的邮箱地址。
现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。
合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。账户本身可以以任意顺序返回。
"""

import collections

class UnionFinder:
    def __init__(self, n):
        self.father = list(range(n))

    def find(self, x):
        if x != self.father[x]:
            self.father[x] = self.find(self.father[x])
        return self.father[x]


    def merge(self, x, y):
        self.father[self.find(x)] = self.find(y)

def accountsMerge(accounts):

    email_index_dict = {}
    email_name_dict = {}
    for account in accounts:
        name = account[0]
        for email in account[1:]:
            if email not in email_index_dict:
                email_index_dict[email] = len(email_index_dict)
                email_name_dict[email] = name

    uf = UnionFinder(len(email_index_dict))
    for account in accounts:
        first_index = email_index_dict[account[1]]
        for email in account[2:]:
            uf.merge(first_index, email_index_dict[email])

    index_to_email_collection = collections.defaultdict(list)
    for email, index in email_index_dict.items():
        index = uf.find(index)
        index_to_email_collection[index].append(email)

    res = []

    for emails in index_to_email_collection.values():
        res.append([email_name_dict[emails[0]]] + sorted(emails))

    return res


def accountsMerge2(accounts):

    def dfs(email, visited, graph, emails):
        if email in visited:
            return
        visited.add(email)
        emails.append(email)
        for neighour in graph[email]:
            dfs(neighour, visited, graph, emails)


    graph = collections.defaultdict(list)
    for account in accounts:
        master = account[1]
        for v in account[2:]:
            graph[master].append(v)
            graph[v].append(master)


    visited = set()
    res = []
    for account in accounts:
        tmp = []
        dfs(account[1], visited, graph, tmp)
        if len(tmp) > 0:
            res.append([account[0]] + sorted(tmp))

    return res


# [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# print(accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]))

# print(accountsMerge([["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"]]))
print(accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]))
print(accountsMerge2([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]))


"""
1.先对原始数据进行整合, 对原始所有的邮箱进行编唯一序号, 对所有的邮箱存放名字
![image.png](https://pic.leetcode-cn.com/1610966328-dGXDAA-image.png)
2.再次对原始数据进行遍历, 使用同一个名字下的邮箱通过唯一序号进行查并集合并
![image.png](https://pic.leetcode-cn.com/1610966919-ISuREf-image.png)
3.最终会归纳为三个独立的分支, 我们将同一个根的序号放到一起.
此时, 我们通过归纳后的index, 取到邮箱的主人名字, 很容易就得到答案了.
"""