# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        itrc = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            itrc+=1
            if fast == slow:
                print(itrc)
                return True
        return False