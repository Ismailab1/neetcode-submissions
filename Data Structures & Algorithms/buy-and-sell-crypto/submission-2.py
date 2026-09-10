class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalGain = 0

        for i in range(len(prices)):
            boughtStock = prices[i]
            for j in range(i + 1, len(prices)):
                maxStock = prices[j]
                totalGain = max(totalGain, maxStock - boughtStock)
        return totalGain