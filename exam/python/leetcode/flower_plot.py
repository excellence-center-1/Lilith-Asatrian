def canPlaceFlowers(flowerbed, n): 
    k = 0
    for i in range(1, n-1):
        if flowerbed[i-1]==0 and flowerbed[i+1]==0:
            flowerbed[i] = 1
            k+=1
    if k==n:
        return True
    return False

print(canPlaceFlowers([1,0,0,0,1], 1))