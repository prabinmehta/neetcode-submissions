class MinStack:

    class Node:
        def __init__(self, val, min_val, prev):
            self.val = val
            self.min_val = min_val
            self.prev = prev

    def __init__(self):
        self.head = None
        

    def push(self, val: int) -> None:
        min_val1 = val if self.head is None else min(self.head.min_val,val)
        self.head = self.Node(val,min_val1, self.head)
        

    def pop(self) -> None:
        self.head = self.head.prev

    def top(self) -> int:
        return self.head.val
        

    def getMin(self) -> int:
        return self.head.min_val
        
