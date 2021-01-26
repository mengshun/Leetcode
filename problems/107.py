"""
107 侧茶树的层序遍历
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
def levelOrderBottom(root):

    if not root:
        return []
    res = []
    queue = collections.deque()
    queue.append(root)
    while queue:
        size = len(queue)
        tmp = []
        for _ in range(size):
            r = queue.popleft()
            tmp.append(r.val)
            if r.left:
                queue.append(r.left)
            if r.right:
                queue.append(r.right)
        res.append(tmp)
    res.reverse()
    return res






node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
print(levelOrderBottom(node1))