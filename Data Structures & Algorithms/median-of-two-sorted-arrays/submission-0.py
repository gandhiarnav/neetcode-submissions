class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge(n1,n2):
            i = 0
            j = 0
            k = 0
            m = []
            while i < len(n1) and j < len(n2):
                if n1[i] < n2[j]:
                    m.append(n1[i])
                    i+=1
                else:
                    m.append(n2[j])
                    j+=1
            while i < len(n1):
                m.append(n1[i])
                i+=1
            while j < len(n2):
                m.append(n2[j])
                j+=1
            return m
        merged_arr = merge(nums1,nums2)
        print(merged_arr)
        n = len(merged_arr)
        res = 0.00
        if n%2 == 0:
            res = (merged_arr[(n//2)-1]+ merged_arr[(n//2)])/2
        else:
            res = merged_arr[(n//2)]

        return res
