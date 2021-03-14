"""
331. 验证二叉树的前序列化
https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree/
"""

from TreeNode import TreeNode

# 栈
def isValidSerialization(preorder):
    arr = preorder.split(",")
    stack = []
    for v in arr:
        stack.append(v)
        while len(stack) >= 3:
            if stack[-1] == "#" and stack[-1] == stack[-2] and stack[-3] != "#":
                stack.pop(-2)
                stack.pop(-2)
            else:
                break
    return len(stack) == 1 and stack[0] == "#"

# 出度入度
def otherFunction(preorder):
    arr = preorder.split(",")
    diff = 1
    for v in arr:
        diff -= 1
        if diff < 0:
            return False
        if v != "#":
            diff += 2
    return diff == 0

print(isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
print(otherFunction("9,3,4,#,#,1,#,#,2,#,6,#,#"))



node9 = TreeNode(9)
node3 = TreeNode(3)
node2 = TreeNode(2)
node9.left = node3
node9.right = node2
node4 = TreeNode(4)
node1 = TreeNode(1)
node3.left = node4
node3.right = node1
node6 = TreeNode(6)
node2.right = node6

def frontBinaryTree(root: TreeNode):

    stack = []
    cur = root
    res = []

    while cur or stack:
        while cur:
            res.append(cur.val)
            stack.append(cur)
            cur = cur.left
        res.append("#")
        t = stack.pop()
        cur = t.right
    res.append("#")
    return res


    # res = []
    # def dp(node):
    #     if not node:
    #         res.append("#")
    #         return
    #     res.append(node.val)
    #     dp(node.left)
    #     dp(node.right)
    # dp(root)
    # return res

print(frontBinaryTree(node9)) # [9, 3, 4, '#', '#', 1, '#', '#', 2, '#', 6, '#', '#']



