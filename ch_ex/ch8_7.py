def make_album(artist, title, num=None) :
    if num :
        album = {"artist" : artist, "title" : title, "Number of songs" : num}
    else :
        album = {"artist" : artist, "title" : title}
    return album

test = make_album("Led Zeppellin", "IV", 9)
print(test)

while True :
    art = input("Enters the albums artist (or q to quit) : ")
    if art == "q" :
        break
    tit = input("Enter the albums title (or q to quit) : ")
    if tit == "q" :
        break
    print(make_album(art,tit))

