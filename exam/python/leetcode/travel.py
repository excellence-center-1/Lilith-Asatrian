    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        min_price = prices[i]
        j = 1
        max_profit = 0
        while j<len(prices):
            if prices[j]<prices[i]:
                i=j
            elif prices[j]-prices[i]>max_profit:
                max_profit = prices[j]-prices[i]
            j+=1
        
        return max_profit