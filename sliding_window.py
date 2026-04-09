# ================================================
# Date: 9 Apr 2026
# Problem: Best Time to Buy and Sell Stock
# Pattern: Sliding Window (single pass)
# Solved alone? Partially — guided
# Key insight: track min_price and max_profit in one loop
# profit = current_price - min_price
# Time: O(n) | Space: O(1)
# ================================================

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for i in prices:
            buy = min(buy, i)
            profit = i - buy
            max_profit = max(max_profit, profit)

        return max_profit