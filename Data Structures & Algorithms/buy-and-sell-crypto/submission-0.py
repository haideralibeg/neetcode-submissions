class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Given a list of prices 
        # if the prices are decending then no profit can be made
        # so it would be either profit or loss
        # if you choose not to buy then 0
        # otherwise you either make money or lose it


        profit = 0
        left = 0 
        
        # start the right right after left at 1
        for right in range(1, len(prices)):

            if prices[right] > prices[left]:

                current_profit = prices[right] - prices[left]
                profit = max(current_profit, profit)
            
            elif prices[right] < prices[left]:

                left = right 

        return profit










