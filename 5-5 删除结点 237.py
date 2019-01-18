# leetcode - 237. Delete Node in a Linked List
# 改变当前结点的值， 链接到下一个结点的next
node.val = node.next.val
node.next = node.next.next
