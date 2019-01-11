# 实现链表的打印
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

arr = [0,1,2,3,4,5]
head = CreateNode(arr)
PrintList(head)
