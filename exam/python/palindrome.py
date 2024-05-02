def palindorme(str):
    if(str[::-1] == str):
        return "It is palindrome"
    else:
        return "It is not palindrome"
    
print(palindorme("annay"))