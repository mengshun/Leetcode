"""
112 路径总和
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, targetSum):
    res = [False]
    def sumTreeNode(tree, target):
        if not tree or res[0]:
            return
        target += tree.val
        if tree.left or tree.right:
            sumTreeNode(tree.left, target)
            sumTreeNode(tree.right, target)
        else:
            if target == targetSum:
                res[0] = True

    sumTreeNode(root, 0)
    return res[0]




node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3

print(hasPathSum(node1, 3))


