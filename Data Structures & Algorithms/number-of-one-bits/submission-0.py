class Solution:
    def hammingWeight(self, n: int) -> int:

        s = ""

        while n!=0:
            
            if n%2==1:
                s+='1'
            else:
                s+='0'
            n = n // 2
        
        s = s[::-1]

        print(s)
        c=0
        for i in s:
            print(i)
            if i == '1':
                c+=1
        return c

