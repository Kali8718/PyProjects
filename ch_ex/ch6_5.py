rivers = {
    'Nile' : 'Egypt',
    'Amazon' : 'Brazil',
    'Yangtze' : 'China',
    'Missisipi' : 'USA',
    'Yenisei' : 'Russia'
}

for river, country in rivers.items() :
    print(f"{river} is situated in {country}")

print('\nlist of rivers :')
for river in rivers.keys() :
    print(river)

print('\nlist of countries with the biggest rivers')
for country in rivers.values() :
    print(country)