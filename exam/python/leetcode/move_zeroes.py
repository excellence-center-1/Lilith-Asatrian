def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    i = 0
    j = 1
    while j < n:
        if nums[j]!=0:
            nums[i], nums[j] = nums[j], nums[i]
        
        j+=1
    return nums
nums = [0,1,0,3,12]
print(moveZeroes(nums))