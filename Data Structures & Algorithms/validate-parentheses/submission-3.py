class Solution:
    def isValid(self, s: str) -> bool:
        dic={'[':']','(':')','{':'}'}
        s = s[::-1]
        stack = []

        for i in s:
            print("call:0",stack)
            if i in dic.values():
                print("call:1",stack)
                stack.append(i)
            if i in dic.keys():
                if stack:
                    print("call:2",stack)
                    if stack[-1] == dic[i]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False 
        print("call:3",stack)

        if stack:
            return False
        else:
            return True

