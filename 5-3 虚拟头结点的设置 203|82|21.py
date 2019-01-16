# Leetcode - 203

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


# Leetcode - 82

# Leetcode - 21
