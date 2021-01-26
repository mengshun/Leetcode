"""
111 二叉树最小深度和最大深度
"""
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # BFS
    def minDepth(self, root: TreeNode):
        if not root:
            return 0

        queue = collections.deque([(root, 1)])
        while queue:
            cur, deep = queue.popleft()
            if not cur.left and not cur.right:
                return deep
            if cur.left:
                queue.append((cur.left, deep + 1))
            if cur.right:
                queue.append((cur.right, deep + 1))
        return 0

    # DFS
    def minDepth2(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        left = float('inf')
        right = float('inf')
        if root.left:
            left = min(self.minDepth2(root.left), left)
        if root.right:
            right = min(self.minDepth2(root.right), right)

        return min(left, right) + 1

    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

