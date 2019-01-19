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
# 空值处理
if head is None:
    return []
# 头结点
dummy_node = ListNode(0)    
# 结果链表的头结点
l2 = ListNode(0)                            
res = l2                                    
dummy_node.next = head                      
# 双指针
n1 = dummy_node                             
n2 = dummy_node      
# 计算链表的长度
i = -1                                      
temp = dummy_node                           
while temp:                                 
    temp = temp.next                        
    i += 1                                  
# print(i)            
# 求余数，减少旋转数目
k = k % i                                   
# print('k = ', k)                            

# n2 指向被删除结点的前一个结点           
for i in range(k+1):           
    n1 = n1.next          
while n1:                 
    n1 = n1.next          
    n2 = n2.next            
# # 最后 delNode 之后的元素删除    
delNode = n2              
while n2.next:            
    l2.next = n2.next     
    l2 = l2.next          
    n2 = n2.next          
delNode.next = None       
l2.next = dummy_node.next 
return res.next

# leetcode - 143

# leetcode - 234
