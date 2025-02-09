nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
nums3 = []
m = 3
n = 3 
j=0
i=0
        
while i<m and j<n:
    if(nums1[i]<=nums2[j]):
        nums3.append(nums1[i])
        i+=1
    else:
        nums3.append(nums2[j])
        j+=1
    
for k in range(j, n):
    nums3.append(nums2[j])
    j+=1
nums1 = nums3

print(nums1)
