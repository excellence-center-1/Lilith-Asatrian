def maxProfit( prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    i = 0
    j = 1
    max_profit = 0
    while j<len(prices):
        if prices[j]<prices[i]:
            i=j
        elif prices[j]-prices[i]>max_profit:
            max_profit = prices[j]-prices[i]
        j+=1
    
    return max_profit

print(maxProfit([2, 1]))