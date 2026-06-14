class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*len(nums)
        postfix=[1]*len(nums)
        prefixProduct,postfixProduct=1,1
        for i in range(len(nums)):
            prefix[i]=prefixProduct
            prefixProduct*=nums[i]
        for i in range(len(nums)-1, -1, -1):
            postfix[i]=postfixProduct
            postfixProduct*=nums[i]
        # print(prefix, postfix)
        output=[]
        for i in range(len(nums)):
            output.append(prefix[i]*postfix[i])
        return output