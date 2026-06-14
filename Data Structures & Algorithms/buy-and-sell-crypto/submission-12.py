class Solution:
    # use sliding window, two pointers, move the right pointer always
    # for left pointer, if right is lower than left, just replace 
    # right with left, look at image in the video
    def maxProfit(self, prices: List[int]) -> int:
        maxP=0
        l,r=0,1
        while(r<len(prices)):
            if(prices[l]<=prices[r]):
                profit=prices[r]-prices[l]
                maxP=max(maxP, profit)
                r+=1
            else:
                # replace right with left
                l=r
                r+=1
        return maxP