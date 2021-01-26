"""
83 删除排序链表中的重复元素
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def deleteDuplicates(head):

    dp = []
    last = ListNode(0)
    pre = head
    while pre:
        if pre.val not in dp:
            dp.append(pre.val)
            last.next = pre
            last = pre
        pre = pre.next
        last.next = None

    return head

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
deleteDuplicates(node1)

while node1:
    print(node1.val)
    node1 = node1.next