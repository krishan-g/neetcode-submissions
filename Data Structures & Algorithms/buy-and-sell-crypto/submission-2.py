class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest = None
        for p in prices:
            if lowest is not None:
                max_profit = max(max_profit, p - lowest)
                lowest = min(lowest, p)
            else:
                lowest = p
        
        return max_profit