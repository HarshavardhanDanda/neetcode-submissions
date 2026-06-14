class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP=0
        minPrice=prices[0]
        for i in range(len(prices)):
            minPrice=min(minPrice, prices[i])
            profit=prices[i]-minPrice
            maxP=max(maxP, profit)
        return maxP
