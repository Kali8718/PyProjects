import random

#Class players to emulate players, each player is an instance

class Players :
    position = 1
    
    def __init__(self, name):
        Players.position += 1
        
        self.name = name
        self.position = Players.position
        self.cards = []       
        
    def normal_pull(self, set) :
        self.cards.append(set.pop())     

    def intitial_pull(self, set) :
        for i in range(0,4) :
            self.normal_pull(set)

            
            



#set of functions to create and shuffle the set

draw_pile = []
discard_pile = []

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




#Section to use the functions 

player_1 = Players('Ali')
player_2 = Players('Othmane')

generate_set(draw_pile)
shuffle_set(draw_pile)

print(player_1.cards)

player_1.intitial_pull(draw_pile)

print(player_1.cards)
