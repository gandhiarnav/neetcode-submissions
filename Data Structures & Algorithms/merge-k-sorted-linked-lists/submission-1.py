# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        tail = list3

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            elif list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        while list1:
            tail.next = list1
            list1 = list1.next
            tail = tail.next
        while list2:
            tail.next = list2
            list2 = list2.next
            tail = tail.next

        return list3.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if not lists[0]:
            return None

        n = len(lists)
        print(n)
        max_l = 0
        for i in range(n):
            cur_l = 0
            itr = lists[i]
            while itr:
                itr = itr.next
                cur_l += 1
            max_l = max(max_l,cur_l)
        print(max_l)
        result = lists[0]
        for i in range(1,n):
            result = self.mergeTwoLists(result, lists[i])

        return result
    
        

            

