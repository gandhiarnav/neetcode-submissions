class Solution:
    def isValid(self, s: str) -> bool:
        def pop(lst):
            return lst.pop()
        def push(lst,item):
            lst.append(item)
            return None
        def top(lst):
            return lst[-1]
        stk=[]
        dic={'[':']','(':')','{':'}'}
        for i in s:
            if i in dic.values():
                print(i)
                if len(stk)==0:
                    return False
                if i== dic[top(stk)]:
                    pop(stk)
                else:
                    return False
            else:
                print(i)
                push(stk,i)
        return True if not stk else False
            

        