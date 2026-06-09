class MinStack:

    def __init__(self):
        self.minstack = [float('inf')]
        self.stack = []

    def push(self, val: int) -> None:

        if min(val,self.minstack[-1]) == val:
            self.minstack.append(val)
            print(val,"pushed to minstack")
        self.stack.append(val)

        # self.minstack.append(min(val,self.minstack[-1])) 
        # print(min(val,self.minstack[-1]),"pushed to minstack")
        # self.stack.append(val)



    def pop(self) -> None:
        val = self.stack.pop()
        if self.minstack[-1] == val:
            self.minstack.pop()
            print(val,"poped")
        return
            
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
