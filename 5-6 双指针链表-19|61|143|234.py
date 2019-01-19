# leetcode - 19
dummy_node = ListNode(0)
dummy_node.next = head
# 双指针
n1 = dummy_node
n2 = dummy_node
# n2 指向被删除结点的前一个结点
for i in range(n+1):
    n1 = n1.next

while n1:
    n1 = n1.next
    n2 = n2.next
delNode = n2.next
n2.next = delNode.next
delNode.next = None
return dummy_node.next


# leetcode - 61

# leetcode - 143

# leetcode - 234
