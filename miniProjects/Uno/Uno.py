import random

set_list = []

colors = ['G','B','Y','R']
numbers = []

for i in range (0,11) :
    numbers.append(i)
    if i == 0 and i in numbers :
        pass
    else :
        numbers.append(i)



def generate_set(set) :
    for number in numbers :
        for color in colors :
            added_card = f'{number}{color}'
            set.append(added_card)
            
def shuffle_set(set) :
    i = 0
    for card in set :
        random_int = random.randint(0,len(set)-1)
        c = set[i]
        set[i] = set[random_int]
        set[random_int] = c
        i += 1
        

def ask_number_players() :
    num_players = input("How many players are in the game ? ")
    print(f"There are {num_players} players in this game")
    return num_players


  

generate_set(set_list)
shuffle_set(set_list)
print(set_list)

