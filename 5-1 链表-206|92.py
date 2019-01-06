# leetcode - 206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        
        pre = None
        cur = head
        
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre
    
# 调试程序——version
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = ListNode(None)
head = a
####

pre = None
cur = head
while cur:
    nex = cur.next
    cur.next = pre
    pre = cur
    cur = nex
print(pre.val)

                
# leetcode - 92. Reverse Linked List II
