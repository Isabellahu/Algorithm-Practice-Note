# 列表转化为链表 CreateNode
# 链表的打印    PrintList    
# 链表的反转    Reverse_list
# Definition for singly-linked list.                  
class ListNode:                                       
    def __init__(self, x):                            
        self.val = x                                  
        self.next = None                              
                                                      
                                                      
# Create                                              
def CreateNode(arr):                                  
    if len(arr) == 0:                                 
        return None                                   
    head = ListNode(arr[0])                           
    curNode = head                                    
    for i in range(1, len(arr)):                      
        curNode.next = ListNode(arr[i])               
        curNode = curNode.next                        
    return head                                       
                                                      
                                                      
def PrintList(curNode):                               
    while curNode is not None:                        
        print(curNode.val, '-> ', end='')             
        curNode = curNode.next                        
    print('null', '\n')                               
                                                      
                                                      
def Reverse_list(head):                               
            cur = head                                
            pre = None                                
            while cur:                                
                nex = cur.next                        
                cur.next = pre                        
                pre = cur                             
                cur = nex                             
            return pre                                
   

# Leetcode - 2. Add Two Numbers                                               
arr = [5]                                             
brr = [5]                                             
l1 = CreateNode(arr)                                                                                      
l2 = CreateNode(brr)                                  
                                                      
# 注意[5] [5] -> [0, 1] 进位的处理                           
# 如果直接将数字相加，大数可能会超出数值范围                               
i = 0                                                 
res = 0                                               
l3 = ListNode(int(res % 10))                          
head = l3                                             
while l1 or l2:                                       
    res = l1.val + l2.val + res                       
    l3.next = ListNode(res % 10)                      
    l1 = l1.next                                      
    l2 = l2.next                                      
    i += 1                                            
    res = res // 10                                   
    l3 = l3.next                                      
                                                      
    while l1 is None and l2:                          
        res = l2.val + res                            
        l3.next = ListNode(res % 10)                  
        l2 = l2.next                                  
        i += 1                                        
        res = res // 10                               
        l3 = l3.next                                  
                                                      
    while l2 is None and l1:                          
        res = l1.val + res                            
        l3.next = ListNode(res % 10)                  
        l1 = l1.next                                  
        i += 1                                        
        res = res // 10                               
        l3 = l3.next         
        
if res != 0:                                          
    l3.next = ListNode(res)                           
PrintList(head.next)               


# Leetcode - 83. Remove Duplicates from Sorted List
# 考虑空值的情况
if head is None:
    return head
pre = head                                        
cur = head           
# 如果 cur=pre.next 会造成最后一个节点为空值的时候直接跳出循环，无法判断前一个节点是否与pre相同
# 故此 cur=pre 使得当最后一个节点和前面节点不同时，新的pre=cur 
while cur:                                        
    if cur.val == pre.val:                        
        cur = cur.next                            
    elif cur.val != pre.val:                      
        pre.next = cur                            
        pre = cur                                 
pre.next = None                                   
return head
    
    
# Leetcode - 86. Partition List
# 给定一个列表和整数 x，将列表中所有小于 x 的元素移到大于或等于 x 的元素前面 
# 用两个链表保存，注意退出循环后自动将末尾链接到None，否则会造成链接到上一次的链表的末尾
h1 = ListNode('na1')                
l1 = h1                             
h2 = ListNode('na2')                
l2 = h2                             
cur = head                          

while cur:                          
    if cur.val < x:                 
        l1.next = cur               
        l1 = l1.next                
    else:                           
        l2.next = cur               
        l2 = l2.next                
    cur = cur.next                  
l2.next = None                      
l1.next = h2.next                   
return h1.next



# Leetcode - 328. Odd Even Linked List
# 给定一个链表，将所有奇数位置节点放在一起，后面放置偶数位置节点。
# 设置一个虚拟的头结点
dummyNode = ListNode(0)
dummyNode.next = head
# 设置一个新的结点，用于链接所有的偶数位置节点
h2 = ListNode('NA')
l2 = h2
cur = dummyNode
# 结点位置指针
i = 0
while cur.next:
    # 偶数位置节点
    if i % 2 != 0:
        delNode = cur.next
        cur.next = delNode.next
        l2.next = delNode
        l2 = l2.next
        delNode.next = None
    # 奇数位置节点
    else:
        cur = cur.next
    i += 1
l2.next = None
cur.next = h2.next
return dummyNode.next


# Leetcode - 445. Add Two Numbers II
# method1
# 通过翻转链表+从末尾开始加和
def reverse_list(head):
    cur = head
    pre = None
    while cur:
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex
    return pre

l1 = reverse_list(l1)
l2 = reverse_list(l2)

res = 0
l3 = ListNode(0)
head = l3

while l1 or l2:
    res = l1.val + l2.val + res
    l3.next = ListNode(res % 10)
    res = res // 10
    l1 = l1.next
    l2 = l2.next
    l3 = l3.next
    # 必须用while，否则会执行前几步的操作短一点的链表值为空报错！
    while l1 and l2 is None:
        res = l1.val + res
        l3.next = ListNode(res % 10)
        res = res // 10
        l3 = l3.next
        l1 = l1.next

    while l2 and l1 is None:
        res = l2.val + res
        l3.next = ListNode(res % 10)
        res = res // 10
        l3 = l3.next
        l2 = l2.next
if res != 0:
    l3.next = ListNode(res)
return reverse_list(head.next)

# method2
stack1 = []
stack2 = []
stack3 = []
while l1:
    stack1.append(l1.val)
    l1 = l1.next
while l2:
    stack2.append(l2.val)
    l2 = l2.next
# 相加的结果
res = 0
while stack1 or stack2:
    res = stack1.pop() + stack2.pop() + res
    stack3.append(res % 10)
    res = res // 10
    # 较为长的链表剩下的结点单独操作
    while stack1 and stack2 == []:
        res = stack1.pop() + res
        stack3.append(res % 10)
        res = res // 10
    # 较为长的链表剩下的结点单独操作
    while stack2 and stack1 == []:
        res = stack2.pop() + res
        stack3.append(res % 10)
        res = res // 10
# 首位进位
if res != 0:
    stack3.append(res)
# 列表到链表
h3 = ListNode(0)
l3 = h3
for i in range(len(stack3)):
    l3.next = ListNode(stack3.pop())
    l3 = l3.next
return h3.next
