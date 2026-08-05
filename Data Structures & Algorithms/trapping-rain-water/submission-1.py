class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxleft = [0 for x in range(n)]
        maxright = [0 for x in range(n)]
        minlr = [0 for x in range(n)]
        
        for i in range(n):
            # print(i)
            if i == 0:
                maxleft[0] = height[i]
            elif maxleft[i-1] < height[i]:
                maxleft[i] = height[i]
            else:
                maxleft[i] = maxleft[i-1]
        for j in range(n):
            # print(j)
            if i == 0:
                maxright[0] = 0
            elif maxright[j-1] < height[n-j-1]:
                maxright[j] = height[n-j-1]
            else:
                maxright[j] = maxright[j-1]

        maxright = maxright[::-1]

        for i in range(n):
            if i == 0:
                minlr[0] = 0
            else:
                minlr[i] = min(maxleft[i],maxright[i])

        


        print(height,"\n",maxleft,"\n",maxright[::-1],"\n",minlr)

        res = 0
        for i in range(n):
            if (minlr[i]-height[i]) > 0:
                res += minlr[i] - height[i]
                print(res,end=' ')

        return res
            
