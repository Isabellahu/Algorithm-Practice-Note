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
    
    
# Leetcode - 86 

# Leetcode - 328 

# Leetcode - 445 
