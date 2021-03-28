"""
83 删除排序链表中的重复元素
"""
from TreeNode import ListNode
print("83. 删除排序链表中的重复元素")
def deleteDuplicatesOne(head):
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

def deleteDuplicatesOneOther(head):
    if not head:
        return None
    pre = head
    current = pre.next
    while current:
        while current and current.val == pre.val:
            current = current.next
        pre.next = current
        pre = current
    return head


node = ListNode(0).initListNode([1,1,2,3,3])
deleteDuplicatesOne(node)
node.printNode()

node = ListNode(0).initListNode([1,1,2,3,3])
deleteDuplicatesOneOther(node)
node.printNode()


"""
82. 删除排序链表中的重复元素 II
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/
"""
print("\n82. 删除排序链表中的重复元素 II")

"""
1.  头节点存在和后面节点重复的可能性, 需要人为创建一个头节点
2.  比较第一个节点和后面节点值是否一样, 直到找到不一样的值为止, 
    搜索结束, 在搜索的过程中发现存在重复节点, 则直接将头节点和当前的相连接,
    不存在重复节点, 则移动头节点
"""
def deleteDuplicatesTwo(head):
    # 迭代
    if not head or not head.next:
        return head

    hair = ListNode(0)
    hair.next = head

    pre = hair
    current = pre.next
    while current:
        while current.next and current.val == current.next.val:
            current = current.next
        if pre.next == current:
            pre = pre.next
        else:
            pre.next = current.next
        current = current.next
    return hair.next

    # # 递归
    # if not head or not head.next:
    #     return head
    # if head.val != head.next.val:
    #     head.next = deleteDuplicatesTwo(head.next)
    # else:
    #     move = head.next
    #     while move and move.val == head.val:
    #         move = move.next
    #     return deleteDuplicatesTwo(move)
    # return head

    # if not head or not head.next:
    #     return head
    #
    # hair = ListNode(0)
    # hair.next = head
    #
    # prepre = hair
    # pre = head
    # current = pre.next
    # while current:
    #     should_skip = False
    #     while current and current.val == pre.val:
    #         should_skip = True
    #         current = current.next
    #     if should_skip:
    #         prepre.next = current
    #     else:
    #         prepre = pre
    #     if current:
    #         pre = current
    #         current = current.next
    # return hair.next




node = ListNode(0).initListNode([1,1,2,3,3])
node = deleteDuplicatesTwo(node)
node.printNode()
node = ListNode(0).initListNode([1,1,1,2,3])
node = deleteDuplicatesTwo(node)
node.printNode()
node = ListNode(0).initListNode([1,2,3,3,4,4,5])
node = deleteDuplicatesTwo(node)
node.printNode()
node = ListNode(0).initListNode([1,2,3,3])
node = deleteDuplicatesTwo(node)
node.printNode()



print("\n\n 测试用例 复习-------")

# 只保留重复的一个元素
def removeDuplicatesOne(head):
    if not head or not head.next:
        return head
    cur = head
    while cur:
        # 1和2的值一样了 就将 1和3相连, 1和3不一样 就移动1的位置到3, 继续3和4进行比较
        if cur.next and cur.next.val == cur.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head


# 重复的一个都不保留
def removeDuplicatesTwo(head):
    if not head or not head.next:
        return head

    #迭代
    """
    1 1 2 3 3
    创建头发节点 连接头节点1
    比较节点1和下个节点值  发现一样 移动节点到 第二个1
    第二个1和下个节点不一致 跳出循环
    判断头节点的下一个和当前节点是否是同一个节点 发现不是 则连接到2节点
    """
    hair = ListNode()
    hair.next = head
    pre = hair
    cur = pre.next
    while cur:
        while cur.next and cur.next.val == cur.val:
            cur = cur.next
        if pre.next == cur:
            pre = cur
        else:
            pre.next = cur.next
        cur = cur.next
    return hair.next


    # # 递归
    # if head.next.val != head.val:
    #     head.next = removeDuplicatesTwo(head.next)
    # else:
    #     move = head
    #     while move.next and move.val == move.next.val:
    #         move = move.next
    #     return removeDuplicatesTwo(move.next)
    # return head


array_list = [[1,1,2,3,3], [1,1,1,2,3], [1,2,3,3,4,4,5], [1,2,3,3]]
test_list = [ListNode(0).initListNode(v) for v in array_list]
for v in test_list:
    print("\n")
    v.printNode()
    res1 = removeDuplicatesOne(v)
    res1.printNode()
    # res2 = removeDuplicatesTwo(v)
    # res2.printNode()

