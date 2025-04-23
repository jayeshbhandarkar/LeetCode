class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        smallest = prices[0]
        max_profit = 0

        for price in prices:
            if price < smallest:
                smallest = price
            else:
                max_profit = max(max_profit, price - smallest)

        return max_profit
