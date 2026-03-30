phones = {
    "Ahmed" : "A5",
    "Amine" : "S20",
    "Hamza" : "P20",
    "Anass" : "Iphone X",
}
list = ['ali','ahmed','Hamza','yasmine','letroll','Anass']
cList = []
for item in list :
    cList.append(item.title())


for person in cList :
    if person.title() not in phones :
        print(f'would you like to register your phone, {person} ?')