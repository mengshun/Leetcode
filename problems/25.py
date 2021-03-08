"""
25. K 个一组翻转链表
"""
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def createNode(self, array):
        if len(array) == 0:
            return None
        node = ListNode(array[0])
        node.next = self.createNode(array[1:])
        return node



def reverseKGroup(head, k):
    if not head:
        return None

    def reverseNode(hd, tail):
        pre = tail.next
        p = hd
        while pre != tail:
            nt = p.next
            p.next = pre
            pre = p
            p = nt
        return tail, hd

    hair = ListNode(0)
    hair.next = head
    pre = hair
    while head:
        tail = pre
        for i in range(k):
            tail = tail.next
            if not tail:
                return hair.next
        nt = tail.next
        head, tail = reverseNode(head, tail)
        pre.next = head
        tail.next = nt
        pre = tail
        head = tail.next

    return hair.next


    return root

def reverseBetween(head, left, right):

    def reverseListNode(head, tail):
        pre = tail.next
        p = head
        while pre != tail:
            nt = p.next
            p.next = pre
            pre = p
            p = nt
        return tail, head

    hair = ListNode()
    hair.next = head

    h = None
    t = None
    last = None

    tmp = hair

    for i in range(right):
        t_last = tmp
        tmp = tmp.next
        if i == left - 1:
            last = t_last
            h = tmp
        elif i == right - 1:
            t = tmp
    h, t = reverseListNode(h, t)
    last.next = h
    return hair.next


node = ListNode()
node = node.createNode([1,2,3,4,5])

# node = reverseKGroup(node, 3)
node = reverseBetween(node, 2, 4)

while node:
    print(node.val)
    node = node.next