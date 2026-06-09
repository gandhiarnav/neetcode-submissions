# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lst = []
        itr = head
        while itr:
            lst.append(itr.val)
            itr = itr.next

        print(lst)

        mid = len(lst)//2
        print(mid)
        for_lst = lst[:mid]
        print(for_lst)
        rev_lst = lst[:mid-1:-1]
        print(rev_lst)
        res_lst = []
        j,k = 0,0
        for i in range(len(lst)):
            if i%2==0 and j<len(for_lst):
                res_lst.append(for_lst[j])
                j+=1
            else:
                if k<len(rev_lst):
                    res_lst.append(rev_lst[k])
                    k+=1
            
        print(res_lst)

        itr = head
        for i in res_lst:
            itr.val = i
            itr = itr.next



        
