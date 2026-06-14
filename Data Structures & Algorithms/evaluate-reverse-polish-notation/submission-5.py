class Solution:
    def calc(self,a,b,op):
        if(op=='+'):
            return a+b
        elif(op == '*'):
            return a*b
        elif(op == '-'):
            return b-a
        else:
            return int(b/a)
    def evalRPN(self, tokens: List[str]) -> int:
        arr=[]
        for i in tokens:
            if(i not in ['*', "+", "-", "/"]):
                arr.append(int(i))
            else:
                a=arr.pop()
                b=arr.pop()
                val=self.calc(a,b,i)
                arr.append(val)
            print(arr)
        return arr[0]

