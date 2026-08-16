class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        profit = 0
        for price in prices:
            profit = max(price - smallest, profit)
            
            if price < smallest:
                smallest = price
            
        return profit