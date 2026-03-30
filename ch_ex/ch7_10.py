vacation = {}
while True :
    name = input('what is your name ?\n')
    place = input('what is your dream vacation location ?\n')
    vacation[name] = place
    answer = input('is someone else taking the survey ? Y/N\n')
    if answer == 'N' or answer.lower() == 'no' :
        break

print("here are the results of the survey : ")
for name, place in vacation.items() :
    print(f"{name} : {place}")
    