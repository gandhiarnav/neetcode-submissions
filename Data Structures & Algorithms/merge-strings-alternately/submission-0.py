class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        i = 0
        j = 0
        li = len(word1)
        lj = len(word2)
        for a in range(li+lj):


            if i < li:
                res += word1[i]
                i+=1
            if j < lj:
                res += word2[j]
                j+=1
        return res