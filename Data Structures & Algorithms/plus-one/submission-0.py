class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = False
        for i in range(len(digits)-1,-1,-1):
            digits[i]+=1

            if digits[i] != 10:
                carry = False
                break
            else:
                carry = True
                digits[i] = 0
        if not carry:
            return digits

        res = [1]
        
        for i in range(len(digits)):
            res.append(0)

        return res
