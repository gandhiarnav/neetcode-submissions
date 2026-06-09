class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_dict={}
        k_out=[]
        for i in range(len(nums)):
            if nums[i] in n_dict:
                n_dict[nums[i]]+=1
            else:
                n_dict[nums[i]]=1

        all_out=[k for k,v in sorted(n_dict.items(),key= lambda x:x[1],reverse=True)]

        for i in range(k):
            k_out.append(all_out[i])
        return k_out



n_dict={}
nums=[]
k=int





# obj = Solution()
# result = obj.topKFrequent(nums,k)
# print(result)