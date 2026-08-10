def reverse(text) :
    char_list = list(text)
    for i in range(len(text)// 2) :
        j = len(text) - 1 - i
        
        char_list[i], char_list[j] = char_list[j], char_list[i]
    
    output = "".join(char_list)
    return output
        
        
print(reverse("mohamed ali"))