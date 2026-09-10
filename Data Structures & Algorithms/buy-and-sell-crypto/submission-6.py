class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]

        for price in prices:
            minBuy = min(minBuy, price)
            maxProfit = max(maxProfit, price - minBuy)
        
        return maxProfit