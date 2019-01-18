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
# method 1
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

# method 2
def PrintList(curNode):
    while curNode is not None:
        print(curNode.val, '-> ', end='')
        curNode = curNode.next
    print('null', '\n')
# 设置虚拟头结点
res = ListNode(0)
res.next = head
# pre为虚拟头结点，cur为head
pre = res
cur = head
temp = head
i = 0
# i为所有节点的总个数
while temp:
    i += 1
    temp = temp.next
# 分组翻转
# 0-1-2-3-4 变成 0-2-1-3-4 再变成 0-3-2-1-4 ，  k=3
while i >= k:
    # 反转链表的操作，执行（k-1）次
    for j in range(k-1):
        # 之后修改链接无法找到 pre.next
        node = pre.next
        # pre.next 需要 cur.next
        pre.next = cur.next
        # cur.next 需要 pre.next.next
        cur.next = pre.next.next
        # pre.next找到之后再次next 到node
        pre.next.next = node
    # print(pre.val)
    # print(cur.val)
    pre = cur
    cur = cur.next
    # i个结点减去已经反转过的k个结点得到剩余节点个数
    i -= k
PrintList(res)


# Leetcode - 147

# Leetcode - 148
# 归并排序
