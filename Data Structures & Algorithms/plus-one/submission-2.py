class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = False
        for i in range(len(digits)-1,-1,-1):
            digits[i]+=1

            if digits[i] != 10:
                return digits
            digits[i] = 0
        digits.reverse()
        digits.append(1)
        digits.reverse()
        return digits