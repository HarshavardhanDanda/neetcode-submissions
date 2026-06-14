class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we need to use the same result array to compute the prefix 
        # and postfix products. first use for loop to go to right
        # and track the products of prefixes of each element on left
        # similarly, use another for loop for postfixes.
        result=[1]*len(nums)
        prev,post=1,1
        for i in range(len(nums)):
            result[i]=prev
            prev=prev*nums[i]
        for j in range(len(nums)-1, -1, -1):
            result[j]*=post
            post=post*nums[j]
        return result