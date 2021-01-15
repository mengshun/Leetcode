"""
124 二叉树最大路径和
本题中，路径被定义为一条从树中任意节点出发，
沿父节点-子节点连接，达到任意节点的序列。
该路径 至少包含一个 节点，且不一定经过根节点。

输入：root = [1,2,3]
输出：6

输入：root = [-10,9,20,null,null,15,7]
输出：42

输入：root = [-5, 20]
输出：20
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root):
    global res
    res = float('-inf')

    def maxValue(node):
        if not node:
            return 0
        left = max(0, max(node.left))
        right = max(0, max(node.right))
        global res
        res = max(res, left+right+node.val)
        return max(left, right) + node.val

    maxValue(root)
    return res
