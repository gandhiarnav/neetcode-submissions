class Solution:
    def isValid(self, s: str) -> bool:
        dic={'[':']','(':')','{':'}'}
        stack = []

        for i in s:
            if i in dic.keys():
                stack.append(i)
            else:
                if stack:
                    ele = stack.pop()
                    if dic[ele] != i:
                        return False
                else:
                    return False
        if stack:
            return False
        return True