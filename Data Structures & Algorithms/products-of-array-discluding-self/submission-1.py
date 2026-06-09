class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        mule=1
        zero_count = 0
        one_zero_mule = 1
        for i in nums:
            if i==0:
                zero_count+=1
        
        if zero_count == 0:
            for i in nums:
                mule*=i
        elif zero_count >=2:
            mule = 0
            for i in range(len(nums)):
                output.append(0)
            return output
        else:
            for i in nums:
                if i!=0:
                    one_zero_mule*=i
            for i in range(len(nums)):
                if nums[i] == 0:
                    output.append(one_zero_mule)
                else:
                    output.append(0)
            return output
            


        for i in nums:
            output.append(int(mule/i))

        return output