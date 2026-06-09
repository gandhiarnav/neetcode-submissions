# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        i = self.lenLL(head)

        itr = head
        prev = None
        while itr:
            if i == n:
                if prev:   
                    prev.next = itr.next
                else:
                    head = itr.next
                return head
            prev = itr
            itr = itr.next
            i-=1
    def lenLL(self, head: Optional[ListNode]) -> int:
        itr = head
        l = 0
        while itr:
            itr=itr.next
            l+=1
        return l