"""
990. 等式方程的可满足性
"""

def equationsPossible(equations):

    if len(equations) < 2:
        return True

    equals = []
    equalsNot = []
    value_index = {}
    for v in equations:
        a, b = v[0], v[-1]
        if a not in value_index:
            value_index[a] = len(value_index)
        if b not in value_index:
            value_index[b] = len(value_index)
        if v[1] == "=":
            equals.append([value_index[a], value_index[b]])
        else:
            equalsNot.append([value_index[a], value_index[b]])

    n = len(value_index)
    father = list(range(n))
    size = [1] * n

    def find(x):
        if x != father[x]:
            father[x] = find(father[x])
        return father[x]

    def merge(x, y):
        x, y = find(x), find(y)
        if x == y:
            return
        if size[x] > size[y]:
            x, y = y, x
        size[y] += size[x]
        father[x] = father[y]

    for x, y in equals:
        merge(x, y)
    for x, y in equalsNot:
        if find(x) == find(y):
            return False
    return True






print(equationsPossible(["a==b","b!=a"])) # False
print(equationsPossible(["b==a","a==b"])) # True
print(equationsPossible(["a==b","b==c","a==c"])) # True