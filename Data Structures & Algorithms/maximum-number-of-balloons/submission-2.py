from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash = {}
        b = "balloon"
        bhash = dict(Counter(b))
        print(bhash)
        for i in text:
            if i in hash:
                hash[i]+=1
            else:
                hash[i] = 1

        print(hash)
        min_count = len(text)
        bc = 0
        for i in bhash:
            if i in hash:
                x = hash[i]//bhash[i]
                min_count = min(x,min_count)
                bc += 1
        
        if bc < 5:
            return 0 
        
        
        return min_count
