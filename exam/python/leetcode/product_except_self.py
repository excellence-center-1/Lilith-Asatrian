def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n  # Ինիցիալիզացնում ենք պատասխան ցուցակը
    
    # Ձախ կողմի արտադրյալները
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]
    
    # Աջ կողմի արտադրյալները
    right_product = 1
    for i in range(n-1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]
    
    return answer

print(productExceptSelf([1,2,3,4]))


def increasingTriplet(nums):
    n = len(nums)
    if n<3:
        return False
    i = 0
    j = 1
    k = 2
    while i<n-2 and j<n-1 and k<n:
        if nums[i]<nums[j]:
            if nums[j]<nums[k]:
                return True
            j+=1
            k+=1
        else:
            i+=1
            j=i+1
            k=j+1
    return False

print(increasingTriplet([20,100,10,12,5,13]))
