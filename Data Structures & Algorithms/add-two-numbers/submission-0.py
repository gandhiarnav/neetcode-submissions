# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i1,i2 = "",""
        
        temp = l1
        while temp:
            i1+=str(temp.val)
            temp = temp.next
        temp = l2
        while temp:
            i2+=str(temp.val)
            temp = temp.next

        i1,i2 = i1[::-1],i2[::-1]
        print(i1,i2)
        res =  int(i1)+int(i2)
        print(res)
        res = str(res)[::-1]
        print(res)
        l3 = ListNode()
        temp = l3

        for i in range(len(res)-1):
            temp.next = ListNode()
            temp = temp.next
        temp = l3
        for i in range(len(res)):
            temp.val = int(res[i])
            temp = temp.next
        

        print(l3)
        temp = l3
        while temp:
            print(temp.val)
            temp= temp.next
        return l3
            
            


        
        