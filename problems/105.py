"""
105. 从前序与中序遍历序列构造二叉树
https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

"""

from TreeNode import TreeNode

def buildTree(preorder, inorder):

    def myBuildTree(p_left, p_right, i_left, i_right):
        if p_left > p_right:
            return None
        # 前序遍历 第一个节点就是根节点
        preorder_root = p_left
        # 从中序遍历中 定位根节点
        inorder_root = index[preorder[preorder_root]]

        # 创建 根节点
        root = TreeNode(preorder[preorder_root])
        # 得到左子节点 数量
        size_left_subtree = inorder_root - i_left
        # 递归地构造左子树，并连接到根节点
        # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
        root.left = myBuildTree(p_left + 1,p_left + size_left_subtree, i_left, inorder_root - 1)
        # 递归地构造右子树，并连接到根节点
        # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
        root.right = myBuildTree(p_left + size_left_subtree + 1, p_right, inorder_root + 1, i_right)
        return root

    n = len(preorder)
    index = {v : i for i, v in enumerate(inorder)}
    return myBuildTree(0, n-1, 0, n-1)



