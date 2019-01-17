# Leetcode - 24
# 设置虚拟头结点
dummy_node = ListNode(0)
dummy_node.next = head
# node1 node2 表示交换的两个结点
node1 = dummy_node.next
# pre需要指向node2而不是node1
pre = dummy_node
while node1 and node1.next:
    node2 = node1.next
    node1.next = node2.next
    node2.next = node1
    pre.next = node2
    pre = node1
    node1 = node1.next
return dummy_node.next


# Leetcode - 25. Reverse Nodes in k-Group
def reverse_list(head):
    cur = head
    pre = None
    while cur:
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex
    return pre

# 使用三个链表：原始链表， 反转链表， 结果链表
res = ListNode(0)
l3 = res

while head:
    i = 0
    dummy_node = ListNode(0)
    l2 = dummy_node
    while i < k and head:
        l2.next = ListNode(head.val)
        l2 = l2.next
        head = head.next
        i += 1
    if i == k:
        res.next = reverse_list(dummy_node.next)
    else:
        res.next = dummy_node.next

    while res.next:
        res = res.next
return l3.next


# Leetcode - 147

# Leetcode - 148
# 归并排序
