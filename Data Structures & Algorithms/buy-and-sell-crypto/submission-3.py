class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_i=0
        max_profit=0
        for sell_i in range(1,len(prices)):
            if prices[buy_i]<=prices[sell_i]:
                profit=prices[sell_i]-prices[buy_i]  
            else:
                buy_i=sell_i
                profit=prices[sell_i]-prices[buy_i]
            max_profit= max(max_profit,profit)
        return max_profit

            

            

        