#testing random stuff

filename = "alice.txt"

with open(filename, encoding="utf-8") as file_object :
    content = file_object.read()
    words = content.split()
    print(len(words))