#Ունենք տեղեկություններ յուրաքանչյուր քաղաքի վերաբերյալ՝ անուն, աշխարհագրական կոորդինատներ(x,y)
#Անհրաժեշտ է գտնել և արտածել ցուցակում առկա բոլոր քաղաքների միջև հեռավորությունները
import math
def cities_distance(x1, x2, y1, y2):
    return round(math.sqrt((x2-x1)**2+(y2-y1)**2), 3)

def add_city():
    city_name = input("Enter city name: ")
    x_coord = float(input(("Enter x coordinate: ")))
    y_coord = float(input("Enter y coordinate: "))
    return city_name, (x_coord, y_coord)

cities = []
n = int(input("Enter the cities quantity: "))
for i in range(n):
    cities.append(add_city())

A = [[0]*n for _ in range(n)]
for i in range(n-1):
    for j in range(i+1, n):
        coord1, coord2 =  cities[i][1], cities[j][1]
        x1, y1 = coord1
        x2, y2 = coord2
        distance = cities_distance(x1, x2, y1, y2)
        A[i][j], A[j][i] = distance, distance

for i in range(n):
    print(A[i])

