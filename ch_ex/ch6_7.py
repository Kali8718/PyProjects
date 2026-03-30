cousin1 = {
    'first_name' : 'Ahmed',
    'last_name' : "Nemrouri",
    'city' : "Casablanca",
    'age' : '41',
}

cousin2 = {
    'first_name' : 'Hamza',
    'last_name' : 'Nemrouri',
    'city' : 'Marrakech',
    'age' : '25',
}

cousin3 = {
    'first_name' : 'Amine',
    'last_name' : "Nemrouri",
    'city' : "Casablanca",
    'age' : '36',
}

cousins = [cousin1, cousin2, cousin3]

for cousin in cousins :
    for key, value in cousin.items() :
        if key == 'first_name' :
            first_name = value
        if key == 'last_name' :
            last_name = value
        if key == 'city' :
            city = value
        if key == 'age' :
            age = value
    print(f"{first_name} {last_name} is my cousin, he lives in {city} and is {age} years old")