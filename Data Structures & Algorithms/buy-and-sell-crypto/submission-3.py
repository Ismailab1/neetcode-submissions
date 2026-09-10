class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp, rp = 0, 1
        maxProfit = 0

        while rp < len(prices):
          if prices[lp] < prices[rp]:
            profit = prices[rp] - prices[lp]
            maxProfit = max(maxProfit, profit)
          else:
            if prices[rp] < prices[lp]:
                lp = rp
          rp += 1
        return maxProfit