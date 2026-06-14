class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we need to iterate through the nums, the key is to check
        # for each num, if there is a previous number existing, if
        # no, it means its start of sequence, we can just create a 
        # set and use a while loop to check if the next sequence is
        # also there in the set, we can increment the count
        k=set(nums)
        longest=0
        for i in nums:
            if(i-1 not in k):
                length=0
                while i+length in k:
                    length+=1
                longest=max(length,longest)
        return longest