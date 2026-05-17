class MinStack:

    def __init__(self):
        self.stack = []
        self.l=-1
        self.min_val = []

    def push(self, val: int) -> None:
        self.l+=1
        self.stack.append(val)
        if self.l==0:
                self.min_val.append(val)
        else:
            self.min_val.append(min(val,self.min_val[self.l-1]))
        # print(self.stack, self.min_val,self.l)
        

    def pop(self) -> None:
        if self.l>=0:
            #self.stack.pop()
            #self.stack[self.l]=-1
            self.l-=1
            self.min_val.pop()
            self.stack.pop()
        # print(self.stack, self.min_val,self.l)
        

    def top(self) -> int:
        if self.l>=0:
            return self.stack[self.l]
        return '-1'
        

    def getMin(self) -> int:
        print(self.min_val)
        if self.l>=0:
            return self.min_val[self.l]
        return -1

        
