"""
108. 将有序数组转换为二叉搜索树
"""

from TreeNode import TreeNode

class Solution:
    def sortedArrayToBST(self, nums: [int]) -> TreeNode:


        def dfs(left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(left, mid-1)
            root.right = dfs(mid+1, right)
            return root
        return dfs(0, len(nums)-1)




t = [-10,-3,0,5,9]
obj = Solution()
node = obj.sortedArrayToBST(t)
node.preorderTraversal()

