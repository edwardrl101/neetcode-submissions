class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1
        while r < len(prices):
            cur = prices[l]
            while r < len(prices) and prices[r] >= prices[l]:
                profit = max(profit, prices[r]-prices[l])
                r += 1
            l, r = r, r + 1
        return profit