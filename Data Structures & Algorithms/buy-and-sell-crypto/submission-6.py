class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # first method is to just loop and find most minimum
        # and also calculate current max profit with that minimum
        # then find the max profit of all
        # maxP=0
        # minPrice=prices[0]
        # for i in range(len(prices)):
        #     minPrice=min(minPrice, prices[i])
        #     profit=prices[i]-minPrice
        #     maxP=max(maxP, profit)
        # return maxP

        # second method is to use two pointers, sliding window
        # declare left and right pointers, loop right until end of list
        # If today’s price is lower than your buy price, then buying today is always better than buying earlier. thats why we do l=r
        l=0
        r=1
        maxP=0
        for r in range(len(prices)):
            if(prices[l]<prices[r]):
                maxP=max(maxP, prices[r]-prices[l])
            else:
                l=r
        return maxP