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
    num_of_cards = len(set)
    for i in range (0, num_of_cards):
        random_num = random.randint(0, num_of_cards-1)
        set[i] , set[random_num] = set[random_num] , set[i]

        

def ask_number_players() :
    num_players = input("How many players are in the game ? ")
    print(f"There are {num_players} players in this game")
    return num_players


  

generate_set(set_list)
shuffle_set(set_list)
ask_number_players()
print(set_list)

