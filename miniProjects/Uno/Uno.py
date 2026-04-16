import random

"""
Functions to be added later:
- Special cards : reverse turn, +2, +4, choose color, etc
- Interface
- Function to initialize the game
- Consolidate the deck creation and shuffling under 1 function -- DONE
"""

# Create one function to initialize the game, the function can regroup all the sub functions (for now: ask player number,
# initilailize their names, distribute their cards, draw on card to discard pile)

#Class players to emulate players, each player is an instance
#position keeps track of the number of created players e.g. ali_1, akram_2, etc.


class Players :
    position = 1
    all_players = []
    
    def __init__(self, name):
        Players.position += 1
        self.name = name
        self.position = Players.position
        self.cards = []       
        Players.all_players.append(self)
        
    def draw_card(self, set) :
        self.cards.append(set.pop(0))     

    def initial_draw(self, set) :
        for i in range(0,4) :
            self.draw_card(set)
            
    def check_card_in_hand(self, card):
        if card.upper() in self.cards :
            return True
        return False
        
    def play_card(self) :
        while True:
            #first we check if the card is in the player's hand (can be re-written as a function later and called)
            while True:
                played_card = input("Select a card to play: ")
                if played_card.upper() in self.cards :
                    print(f"{self.name} has played {played_card}")
                    break
                else :
                    print(f"card not in hand, re-enter it {[self.cards]}")
            #Now we check if the played card is correct to play
            for char in played_card:
                if char in discard_pile[-1] :
                    discard_pile.append(played_card)
                    return
            print("Card can not be played, please Select an appropriate card or Draw one")
            

        

#set of functions to create and shuffle the set

draw_pile = []
discard_pile = []
number_of_players = 0



def generate_set(set) :
    colors = ['G','B','Y','R']
    numbers = []
    
    for i in range (0,11) :
        numbers.append(i)
        if i == 0 and i in numbers :
            pass
        else :
            numbers.append(i)
    
    for number in numbers :
        for color in colors :
            added_card = f'{number}{color}'
            set.append(added_card)
    
    return set
            

def shuffle_set(set) :
    num_of_cards = len(set)
    for i in range (0, num_of_cards):
        random_num = random.randint(0, num_of_cards-1)
        set[i] , set[random_num] = set[random_num] , set[i]
        
        
def draw_initial_discard_pile(set) :
    discard_pile.append(set.pop(0))
    print(f"The initial card has been played: {discard_pile[-1]}")



            
            
def ask_player_names() :
    player_names = []
    i = 0

    while True :
        name = input(f"Enter the name of player {i+1}, type done when you have inputed all the names: \n")
        if name.lower() == 'done' and i >= 2 :
            break
        elif name.lower() == 'done' and i < 2 :
            print(f"The game needs a minimum of 2 players, you have only entered {len(player_names)}")
        elif name[0].isalpha():
            player_names.append(name)
            i+=1
        else:
            print("The name cannot start with a digit")
    
    print(f"There are {len(player_names)} players in this game")
    print(player_names)
    return player_names




def initialize_game():
    generate_set(draw_pile)
    shuffle_set(draw_pile)
    player_names = ask_player_names()
    draw_initial_discard_pile(draw_pile)
    
        
    
#fuck around and find out section

player_1 = Players('Ali')
player_2 = Players('Akram')

initialize_game()

"""
generate_set(draw_pile)
shuffle_set(draw_pile)
print(draw_pile)

print(player_1.cards)

player_1.initial_draw(draw_pile)

print(player_1.cards)

print(discard_pile)
draw_initial_discard_pile(draw_pile)
print(f"Last played card: {draw_pile[-1]}")


while True :
    for player in Players.all_players:
        print(f"This is {player.name}'s turn")
        player.play_card()
"""