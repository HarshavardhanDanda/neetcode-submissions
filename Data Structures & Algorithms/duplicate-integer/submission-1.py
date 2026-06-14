class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if (i in d):
                return True
            else:
                d[i] = 1
        return False
        
# add counts to a dictionary for each number 
# return true if it is already present in dictionary