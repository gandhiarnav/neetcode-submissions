class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = False
        for i in range(len(digits)-1,-1,-1):
            digits[i]+=1

            if digits[i] != 10:
                return digits
            digits[i] = 0

        res = [1]
        
        res.extend(digits)

        return res
