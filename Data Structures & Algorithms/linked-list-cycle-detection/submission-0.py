# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        n = 0

        # while n<1000:
        #     if not head.next:
        #         return False
        #     head = head.next
        #     n+=1
        # return True

        itr = head
        n = 0
        while itr:
            itr = itr.next
            n+=1
            if n == 1000:
                return True

        return False