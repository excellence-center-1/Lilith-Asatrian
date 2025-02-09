#Ներմուծվում է ո-ն, որը քառակուսի զանգվածի չափն է, և num-ը։
# Երկչափ զանգվածը անհրաժեշտ է լրացնել հետևյալ կերպ․ 
# օժանդակ անկյունագծից վերև լրացնել num-ը  գերազանցող զույգ թվերով, 
# անկյունագծի վրա հաջորդ զույգ թիվը՝ կրկնելով այն ամբողջ անկյունագծի վրա, 
# անկյունագծից ներքև՝ հաջորդ զույգ թվերով։ 
# Ընդ որում՝ անհրաժեշտ զույգ թվերը գեներացնել առանձին ֆունկցիայի միջոցով։
def even_nums(num, k):
    A = []
    start = num+1
    if start%2!=0:
        start+=1
    for _ in range(k):
        A.append(start)
        start+=2
    return A

n = int(input("n="))
num = int(input("num="))
k = n*n-n+1
mid = k//2
even_nums_list = even_nums(num, k)
z = even_nums_list.pop(mid)
print(even_nums_list)
A = []
k = 0
d = 0
for i in range(n):
    row = []
    for j in range(n):
        if i+j==n-1:
            row.append(z)
        elif i+j<n-1:
            row.append(even_nums_list[k])
            k+=1
        else:
            row.append(even_nums_list[mid+d])
            d+=1
    A.append(row)

for i in range(n):
    print(A[i])
        