class Solution:
    # def isValid(self, s: str) -> bool:
    #     stack = []
    #     closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

    #     for c in s:
    #         if c in closeToOpen:
    #             if stack and stack[-1] == closeToOpen[c]:
    #                 stack.pop()
    #             else:
    #                 return False
    #         else:
    #             stack.append(c)

    #     return True if not stack else False
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(s,openc,close):
            if len(s) == 2*n:
                print(s)
                
                res.append(s[::])
                return
            if openc < n:
                backtrack(s+'(',openc+1,close)
            if close < openc:
                backtrack(s+')',openc,close+1)

            
        backtrack("",0,0)
        return res