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


# Leetcode - 25

# Leetcode - 147

# Leetcode - 148
# 归并排序
