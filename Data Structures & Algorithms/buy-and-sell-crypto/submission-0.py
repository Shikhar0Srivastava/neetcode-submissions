class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        max_profit = 0
        buy = 0
        sell = 1
        while(buy < sell and sell < len(prices)):
            profit = max(0, prices[sell] - prices[buy])
            max_profit = max(profit, max_profit)
            
            if prices[buy] > prices[sell]:
                buy += 1
                sell += 1
            else:
                sell += 1
        return max_profit
        