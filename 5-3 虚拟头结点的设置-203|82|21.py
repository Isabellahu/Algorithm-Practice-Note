# Leetcode - 203. Remove Linked List Elements
# # method 1
# 如果头结点不为空且头结点的值为目标值
while head is not None and head.val == val:
    head = head.next
# 如果循环之后头结点为空
if head is None:
    return head
# 循环遍历头结点之后的结点
cur = head
while cur.next:
    if cur.next.val == val:
        delNode = cur.next
        cur.next = delNode.next
        # 内存释放
        delNode.next = None
    else:
        cur = cur.next
return head

# # method 2
# 创建虚拟头结点
dummyNode = ListNode(0)
dummyNode.next = head
cur = dummyNode
while cur.next:
    if cur.next.val == val:
        delNode = cur.next
        cur.next = delNode.next
        # 内存释放
        delNode.next = None
    else:
        cur = cur.next
return dummyNode.next


# Leetcode - 82. Remove Duplicates from Sorted List II
# 新建链表，表头为 dummy_node
dummy_node = ListNode(0)
# pre 为不重复的结点
pre = dummy_node
# cur 为同值结点的开头
cur = head
while cur:
    # nex 为下一个值的结点开头 ， cur和nex之间是同值的结点，前闭后开
    nex = cur.next
    while nex and cur.val == nex.val:
        nex = nex.next
    # cur.val != cur.next.val 同值没有出现两次及其以上
    # cur.next is None  最后一个同值结点开头的下一个结点若为空，则只出现过一次
    if cur.next is None or cur.val != cur.next.val:
        pre.next = ListNode(cur.val)
        pre = pre.next
    cur = nex
return dummy_node.next


# Leetcode - 21
# 递归的方式，返回链表１和２中指针指向的较小的值
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        if l1.val <= l2.val:
            head = l1
            head.next = self.mergeTwoLists(l1.next, l2)
        else:
            head = l2
            head.next = self.mergeTwoLists(l1, l2.next)
        return head
