
def maxProfit(prices):
    max = 0
    for i in range(1, len(prices)):
        if prices[i]>prices[i-1]:
            max+=prices[i]-prices[i-1]
    return max

    

print(maxProfit([1,2,3,4,5]))
        


        