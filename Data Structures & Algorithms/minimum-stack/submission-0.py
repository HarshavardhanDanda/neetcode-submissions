class MinStack:

    def __init__(self):
        self.arr=[]

    def push(self, val: int) -> None:
        self.arr.append(val)

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        l=len(self.arr)
        return self.arr[l-1] if l>0 else None

    def getMin(self) -> int:
        min=float("inf")
        for i in self.arr:
            if(i<min):
                min=i
        return min
