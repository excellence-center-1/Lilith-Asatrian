my_dict = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9
}
try:
    s = input("Enter the text: ")
    new_s = ""
    k = input("Enter the text to be found")
    k_l = len(k)
    new_k = ""
    q = 0
    L = []
    if len(k)>len(s):
        raise Exception("The length of text to be found is bigger than the text")
    for i in range(len(s)):
        l = s[i]
        new_s+=str(my_dict[l])
    for i in range(len(k)):
        l = k[i]
        new_k+=str(my_dict[l])
    new_k = int(new_k)
    for i in range(0, len(s)-k_l+1):
        l = new_s[i:i+k_l]
        if int(l)==new_k:
            q+=1
            L.append(i)
    print("Quantity: ", q)
    print("L: ", L)



except Exception as e:
    print(f"Unexpected exception occured: {e}")