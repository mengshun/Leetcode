"""
2. 两数相加 链表
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def addTwoNumbers(l1, l2):
    pre = None
    root = None
    flag = 0
    while l1 or l2:
        val1 = 0
        val2 = 0
        if l1:
            val1 = l1.val
        if l2:
            val2 = l2.val
        res = val1 + val2 + flag
        cur = ListNode(res % 10)
        if pre != None:
            pre.next = cur
        else:
            root = cur
        pre = cur

        flag = res // 10

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        if not l1 and not l2 and flag > 0:
            t = ListNode(flag)
            pre.next = t


    return root