class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        maxdiff=0
        while(i<len(prices)-1):
            j=i+1
            while(j<len(prices)):
                if(prices[j]>prices[i]):
                    diff=prices[j]-prices[i]
                    maxdiff=max(diff, maxdiff)
                j+=1
            i+=1
        return maxdiff
