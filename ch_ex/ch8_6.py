def city_country(city, country="morocco") :
    x = f"{city}, {country}"
    return x.title()

test = city_country("rabat")
print(test)

test = city_country("paris","france")
print(test)

test = city_country("madrid","spain")
print(test)