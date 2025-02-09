#Կազմել ծրագիր,որը կհաշվի և կտպի տրված x  և y 
# n ամբողջ տարրեր պարունակող միաչափ զանգվածների x զանգվածի 
# կենտ արժեք ունեցող տարրերի և yի զույգ արժեք ունեցող տարրերի գումարների տարբերություն
# A = [[1,2,3],[4,5,6]]

# for i in range(len(A)):
#     for j in range(len(A[i])):
#         print(A[i][j], end=' ')
#     print()

# for row in A:
#     for elem in row:
#         print(elem, end=' ')
#     print()
# n = 2
# m = 3

# A = []
# for i in range(n):
#     A.append([0]*m)

# B = [[0]*m for i in range(n)]

# for i in B:
#     print(i)

# import locale

# locale.setlocale(locale.LC_ALL)

# money = 125.36

# formatted = locale.currency(money)
# print(formatted)

# formatted = locale.format_string('%e', money)
# print(formatted)

# print(locale.getlocale())

# number = 0.1+0.1+0.1
# print(round(number, 2))

# from decimal import Decimal

# number = Decimal("0.100")

# number+=4+number
# print(number)

# number1 = Decimal("5.99")
# print(number1.quantize(Decimal("1.0")))


from decimal import Decimal, ROUND_FLOOR

number = Decimal("9.005")
print(number.quantize(Decimal('1.00'), ROUND_FLOOR))
