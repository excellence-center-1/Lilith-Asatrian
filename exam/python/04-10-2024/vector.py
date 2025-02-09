try:
    n = int(input("Input the size of vector: "))
    if n <= 0:
        raise Exception("The size of vector must me positive integer!")
    x = [int(input(f"{i+1} number: ")) for i in range(n)]
    y = []
    max_num = max(x)
    max_i = x.index(max_num)
    if max_i == 0:
        print("No element before maximum.")
        exit()
    for i in range(1, max_i, 2):
        y.append(x[i] + max_num/2)
    print(y)
except ValueError as e:
    print("Conversion failed: ", e)
