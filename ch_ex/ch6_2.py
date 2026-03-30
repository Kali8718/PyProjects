favNum = {
    "a" : [15,48],
    "b" : [19,89],
    "c" : [94,63],
    "d" : [92,58],
    "e" : [57,25],
}

for person, number in favNum.items() :
    print(f"{person}'s favorite numbers are {(number[0])} and {(number[1])}")