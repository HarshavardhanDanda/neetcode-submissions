# we can solve with brute force but in O(n), we need to use a stack
# use a while loop, keep pushing each element into stack in format 
# [data, index], in the while loop, if we find greater element, keep
# popping the stack, update the output of that index with currentIndex -
# popped index.
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
