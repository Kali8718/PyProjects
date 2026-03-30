#program that outputs a dictionary with how many times a word has been repeated in a txt file

filename = 'alice.txt'
word_count = {}

with open(filename, encoding="utf-8") as file_object :
    contents = file_object.read()
    words = contents.split()
    print(type(words))
    print(len(words))
    for word in words :
        word = word.lstrip()
        if word in word_count :
            word_count[word] += 1
        else :
            word_count[word] = 1


sorted_dict = dict(sorted(word_count.items(), key=lambda item: item[1]))

for key in sorted_dict :
    print(key, ": ",word_count[key])


