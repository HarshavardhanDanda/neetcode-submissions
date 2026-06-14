# you have to maintain two stacks, stack and minStack
# append normal elemetns to stack, append minimum value at that point 
# in minStack
# btw, you can use min function and arr[-1] to get the top element
class MinStack:

    def __init__(self):
        self.arr=[]
        self.minStack=[]

    def push(self, val: int) -> None:
        self.arr.append(val)
        l=len(self.minStack)
        if(len(self.minStack)==0):
            self.minStack.append(val)
            return
        if(val<self.minStack[l-1]):
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[l-1])

    def pop(self) -> None:
        self.arr.pop()
        self.minStack.pop()

    def top(self) -> int:
        l=len(self.arr)
        return self.arr[l-1] if l>0 else None

    def getMin(self) -> int:
        l=len(self.minStack)
        return self.minStack[l-1] if l>0 else None
