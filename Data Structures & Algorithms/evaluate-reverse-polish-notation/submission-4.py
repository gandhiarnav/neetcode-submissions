class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        num_stk = []
        opp_stk=[]
        for i in tokens:
            if i.lstrip('-').isdigit():
                num_stk.append(int(i))
            else:
                a=num_stk.pop()
                b=num_stk.pop()
                if i == "+":
                    num_stk.append(b+a)
                elif i == "-":
                    num_stk.append(b-a)
                elif i == "*":
                    num_stk.append(b*a)
                else:
                    num_stk.append(int(b/a))
        return int(num_stk[-1])