class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def preorderTraversal(self):
        res = []
        def dfs(root: TreeNode):
            if not root:
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(self)
        print("二叉树 前序遍历: " + "  " + str(res))
        return res

    def centerorderTraversal(self):
        res = []
        def dfs(root: TreeNode):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(self)
        print("二叉树 中序遍历: " + "  " + str(res))
        return res

    def postorderTraversal(self):
        res = []
        def dfs(root: TreeNode):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        dfs(self)
        print("二叉树 后序遍历: " + "  " + str(res))
        return res


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printNode(self):
        res = []
        current = self
        while current:
            res.append(current.val)
            current = current.next
        print("链表: " + "  " + str(res))

    def initListNode(self, nums):
        head = ListNode(0)
        pre = head
        for v in nums:
            cur = ListNode(v)
            pre.next = cur
            pre = cur
        print("装载链表完成: " + str(nums))
        return head.next



