bigCities = {
    "Tokyo" : {
        "population" : 37_400_068,
        "country" : "Japan",
        "Definition" : "Metropolis prefecture",
    },
    "Delhi" : {
        "population" : 28_514_000,
        "country" : "India",
        "Definition" : "Capital city",
    },
    "Seoul" : {
        "population" : 25_647_800,
        "country" : "South korea",
        "Definition" : "Special city",
    },
}

for city, chars in bigCities.items() :
    for key, value in chars.items() :
        if key == "population" :
            population = value
        if key == "country" :
            country = value
        if key == "Definition" :
            definition = value
    print(f"{city} is a city in {country} with a population of {population} and has the national status"
        f"of a {definition}")