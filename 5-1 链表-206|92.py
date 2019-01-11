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
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return None
        # 如果m=1,需要添加一个节点连接到第一个节点
        dummy = ListNode(0)          
        dummy.next = head            

        pre = dummy                                              
        i = 1                                    
        # pre 找到ｍ                                
        while pre and i < m:                   
            pre = pre.next                       
            i += 1                               
        # 记录pre                                  
        target = pre                             

        cur = pre.next                           
        while cur and i < n:                   
            nex = cur.next                       
            cur.next = nex.next                  
            nex.next = pre.next                  
            pre.next = nex                       
            i += 1                               

        return dummy.next
    
