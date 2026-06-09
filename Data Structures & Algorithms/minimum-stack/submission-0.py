class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.min = val
        else:
            self.min = min(val,self.min)
        self.stack.append(val)
    def pop(self) -> None:
        val = self.stack.pop()
        if self.min != val:
            return
        else:
            self.min = float('inf')
            for i in self.stack:
                if i < self.min:
                    self.min = i
            
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
        
