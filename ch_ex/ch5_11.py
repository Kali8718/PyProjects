numbers = [a for a in range(1,101)]

for number in numbers :
    if number == 1 :
        print(f"{number}st")
    elif number == 2 :
        print(f"{number}nd")
    elif number == 3 :
        print(f"{number}rd")
    else :
        print(f"{number}th")