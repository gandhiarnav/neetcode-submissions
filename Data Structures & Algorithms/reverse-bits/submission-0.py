class Solution:
    def reverseBits(self, n: int) -> int:
        # print(bin(n))
        b = bin(n)[2:]
        mb = ""
        # print(b)
        mb = '0'*(32-len(b))

        sb= mb+b
        # print(sb)
        rb = sb[::-1]
        # print(rb)
        # # final = "0b"+rb
        return(int(rb,2))
        