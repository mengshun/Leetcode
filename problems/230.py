"""
230. 二叉搜索树中第K小的元素  https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/
"""
from TreeNode import TreeNode
def kthSmallest(root, k):

    stack = []
    res = []

    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        tmp = stack.pop()
        res.append(tmp.val)
        if len(res) == k:
            return res[-1]
        cur = tmp.right
    return 0



node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node3.left = node1
node3.right = node4
node1.right = node2

node3.preorderTraversal()
node3.centerorderTraversal()
node3.postorderTraversal()
print(kthSmallest(node3, 3))
