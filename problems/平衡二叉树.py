
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root):

    global res
    res = True
    def dfs(tree):
        global res
        if tree == None:
            return 0
        left = dfs(tree.left)
        right = dfs(tree.right)
        if abs(left - right) > 1:
            res = False
        return max(left, right) + 1
    dfs(root)
    return res

def isBalanced2(root):
    if not root:
        return True
    return abs(deepth(root.left) - deepth(root.right)) <= 1 and isBalanced(root.left) and isBalanced(root.right)
def deepth(root):
    if not root:
        return 0
    return max(deepth(root.left), deepth(root.right)) + 1
