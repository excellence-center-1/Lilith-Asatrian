def text_analysis(llist):
    my_dict = {}
    for i in llist:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    return my_dict
   
text = input("Input text: ")
my_list = text.split()
print(text_analysis(my_list))