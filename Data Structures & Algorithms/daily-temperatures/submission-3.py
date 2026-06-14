class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        stack = []
        for i,d in enumerate(temperatures):
            while(stack and d > stack[-1][0]):
                stackd,stacki=stack.pop()
                output[stacki]=i-stacki
            stack.append([d,i])
        return output
