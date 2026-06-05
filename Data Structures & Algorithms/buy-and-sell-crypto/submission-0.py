class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_i=0
        sell_i=1
        max_profit=0
        while sell_i<len(prices):
            profit=prices[sell_i]-prices[buy_i]
            max_profit= max(max_profit,profit)
            if prices[buy_i]<=prices[sell_i]:
                sell_i+=1
            elif prices[buy_i]>prices[sell_i]:
                buy_i=sell_i
                sell_i+1
        return max_profit

            

            

        