def remove_suffix_ness(word):
    modified_word = word[:-4]
    
    if modified_word[-1] == "i":
        modified_word = modified_word[:-1] + "y"
    return modified_word

x = remove_suffix_ness("happiness")
print(x)