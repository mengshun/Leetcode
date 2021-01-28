"""
160 相交链表
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None

    # 哈希表解法
    # dp = {}
    # a = headA
    # while a:
    #     dp[a] = 1
    #     a = a.next
    # b = headB
    # while b:
    #     if b in dp:
    #         return b
    #     b = b.next
    # return None

    pa = headA
    pb = headB

    while pa != pb:
        pa = headB if not pa else pa.next
        pb = headA if not pb else pb.next

    return pa



node1 = ListNode(0)
node2 = ListNode(9)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
node4 = ListNode(3)
node5 = ListNode(2)
node4.next = node5
node3.next = node5
node6 = ListNode(4)
node5.next = node6

res = getIntersectionNode(node1, node4)
if res:
    print(res.val)
else:
    print("没有找到")


"""
如果两个链表相交，那么相交点之后的长度是相同的

我们需要做的事情是，让两个链表从同距离末尾同等距离的位置开始遍历。这个位置只能是较短链表的头结点位置。
为此，我们必须消除两个链表的长度差

指针 pA 指向 A 链表，指针 pB 指向 B 链表，依次往后遍历
如果 pA 到了末尾，则 pA = headB 继续遍历
如果 pB 到了末尾，则 pB = headA 继续遍历
比较长的链表指针指向较短链表head时，长度差就消除了
如此，只需要将最短链表遍历两次即可找到位置

"""