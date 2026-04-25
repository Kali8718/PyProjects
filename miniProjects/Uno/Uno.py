import random, time, re
from rich.console import Console
from rich.text import Text


"""

Immediate next steps:
implement a skip round function that gets played on special cards, starting with draw 2, then implement same for a skip card, logic should handle overriding with own +2



Functions to be added later:
- Verify choice function works well by playing more, clean up the text output in the terminal -- Done (text can be cleaned more)
- Special cards : reverse turn, +2, +4, choose color, etc
- Interface
- Function to initialize the game -- DONE
- Consolidate the deck creation and shuffling under 1 function -- DONE
- Choice function with Players class that will allow players to select (draw, play card) -- DONE
- functions to clear the discard while keeping the last card when draw is empty, shuffle it and send it to the draw pile
- turn ask players name to a class method 
- add points logic and multiple rounds, use json file to store the players and allow em to resume ongoing games
- create BOTS YOU CAN PLAY AGAINST
- Create GUI
- Add colors for cards in terminal (maybe a logic that convers 4B to 4 Blue colored)
- refactoring

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
        
    def draw_card(self, draw, number_of_draws) :
        for i in range(0,number_of_draws):
            self.cards.append(draw.pop(0))     

    def initial_draw(self, draw) :
        self.draw_card(draw_pile, 4)
        
            
    def check_card_in_hand(self, card):
        if card.upper() in self.cards :
            return True
        return False
    
    def check_playable_card(self, card, last_discarded) :
        if card[0].upper() == last_discarded[0].upper() :
            return True
        elif card[-1].upper() == last_discarded[-1].upper() :
            return True
        return False
    
    def play_card(self, card, discard) :
        #append the discard card to the discard pipe and pop the card from hand (index is used to return a number as pop accepts only nums)
        discard.append(card)
        self.cards.remove(card)
        
    def check_if_special_card(self, card):
        #checks if the card is a special card
        if len(card) > 2:
            return True
        return False
        
            
    def modify_flag(self, card) :
    #function that sets the flag for the next player for a special card
        if "Draw 2".upper() in card :
            return "D2"
        elif "Draw 4".upper() in card:
            return "D4"

    
    def check_flag_and_act(self, draw, flag_func) :
    #checks if the player has an action card from the previous player and resets the flag
        if flag_func == "D2":
            self.draw_card(draw, 2)
            print("The next player will draw 2 cards")
        elif flag_func == "D4":
            self.draw_card(draw, 4)
            print("The next player will draw 4 cards")
        return None
                     

    def play_or_draw(self, draw, discard, last_discard, flag) :
        
        # functions either lets the player draw or play card
        # if the players draws then a card is appended to his cards and removed from the draw
        while True :
            #check if the player is affected by a previous action card, if flag is none play normally, if its not do the action
            if flag == None:
                choice = input("Type the card you want to play (e.g. 8G, 7B, ReverseB) or type D to draw \n")
                
                if choice.upper() == "D" :
                    self.draw_card(draw, 1)
                    print(f"{self.name} drew a card")
                    break
                    
                else:    
                    if self.check_card_in_hand(choice) :
                        if self.check_playable_card(choice, last_discard) :
                            if self.check_if_special_card(choice) :
                                self.play_card(choice, discard)
                                return self.modify_flag(choice)
                            else:
                                self.play_card(choice, discard)
                                break
                        print("This card is not a correct play")
                    elif not self.check_card_in_hand(choice) :
                        print("You don't have this card")
            else :
                self.check_flag_and_act(draw, flag)
            


#Code I don't understand much to color the outputs

console = Console()

COLOR_MAP = {
    "G": "green",
    "B": "blue",
    "Y": "yellow",
    "R": "red",
}

def color_text(input_data: str | list) -> None:
    """
    Print colored text based on the last character of each string.
    - G → green
    - B → blue
    - Y → yellow
    - R → red
 
    Accepts a single string or a list of strings.
    """
    if isinstance(input_data, list):
        for item in input_data:
            _print_colored(item)
    else:
        _print_colored(input_data)

def _print_colored(text: str) -> None:
    last_char = text[-1].upper() if text else ""
    color = COLOR_MAP.get(last_char)
 
    if color:
        console.print(Text(text[:-1], style=color))
    else:
        # No matching color key — print as-is with a warning
        console.print(text)
        console.print(
            f"  [dim](no color rule for last char: {repr(last_char)})[/dim]"
        )

def print_inline_list(items: list) -> None:
    """
    Print a list of strings inline on a single line, separated by spaces.
    Each item is colored based on its last character (G/B/Y/R).
    """
    for i, item in enumerate(items):
        last_char = item[-1].upper() if item else ""
        color = COLOR_MAP.get(last_char)
        is_last = i == len(items) - 1
        console.print(Text(item[:-1], style=color or ""), end="" if is_last else " | ")
    console.print()  # final newline



#set of functions to create and shuffle the set

draw_pile = []
discard_pile = []
players = []
turn = 0
direction = 1 #1 for normal order, - 1 for opposite order when a reverse card is used. reverse cards not added for now
flag = None



def generate_set(set) :
    colors = ['G','B','Y','R']
    action_cards = ['Draw 2'] # S: Skip, R: Reverse, +2: Draw 2
    numbers = []
    
    for i in range (0,10) :
        numbers.append(i)
        if i == 0 and i in numbers :
            pass
        else :
            numbers.append(i)
    
    for color in colors :
        for number in numbers :
            card = f"{number}{color}"
            set.append(card.upper())
        
        for action_card in action_cards:
            card = f"{action_card}{color}"
            set.append(card.upper())
            set.append(card.upper())

    
    print(set)
    print_inline_list(set)
    
    return set
            

def shuffle_set(set) :
    num_of_cards = len(set)
    for i in range (0, num_of_cards):
        random_num = random.randint(0, num_of_cards-1)
        set[i] , set[random_num] = set[random_num] , set[i]
        
        
def draw_initial_discard_pile(set, discard) :
    discard_pile.append(set.pop(0))
    console.print(f"The initial card has been played: {discard[-1]}")


def show_last_discarded(discard):
    print(f"Card on table: ",end="")
    _print_colored(f"{discard[-1]}")
    
def check_if_draw_pile_empty_then_shuffle(draw, discard) :
    # checks if the draw pile has emptied, if true takes all the cards except the last from discord, shuffles and sends em to draw
    if len(draw) == 0 :
        draw.extend()
        del discard[0:-1]
        shuffle_set(draw)
        print("The remainig discard pile has been reshuffled and re-added to be drawn")
            
            
def ask_player_names() :
    player_names = []
    i = 0

    while True :
        name = input(f"Enter the name of player {i+1}, type done or x when you have inputed all the names: \n")
        if (name.lower() == 'done' or name.lower() == 'x') and i >= 2 :
            break
        elif (name.lower() == 'done' or name.lower() == 'x') and i < 2 :
            print(f"The game needs a minimum of 2 players, you have only entered {len(player_names)}")
        elif name[0].isalpha():
            player_names.append(name)
            i+=1
        else:
            print("The name cannot start with a digit")
    
    print(f"There are {len(player_names)} players in this game")
    for i, name in enumerate(player_names) :
        print(f"Player {i+1}: {name}")
    return player_names




def initialize_game(draw, discard):
    #includes generating the set, shuffling it, creating the players, serving them cards
    generate_set(draw)
    shuffle_set(draw)
    player_names = ask_player_names()
    draw_initial_discard_pile(draw, discard)
    for name in player_names :
        players.append(Players(name))
    
    for player in players:
        player.initial_draw(draw)


    
#fuck around and find out section

#my current idea is to use a dictionary and assign a number to each number, then we can use an i to increment or decrement
# we can honestly also do this with a list and use the i as the index, much simpler
#another idea would be to use a while loop (gpt idea not mine)
initialize_game(draw_pile, discard_pile)

while len(players) > 1 :
    print("-----------------------------------------------------------------------------")
    
    #append code for debugging, will be removed later
    
    flag = players[turn].check_flag_and_act(draw_pile, flag)    
    
    print(f"This is {players[turn].name}'s turn, available cards are")
    print_inline_list(players[turn].cards)
    show_last_discarded(discard_pile)
    flag = players[turn].play_or_draw(draw_pile, discard_pile, discard_pile[-1], flag)
    print(f"flag = {flag}")

    print(f"{players[turn].name}'s new cards are: ", end="")
    print_inline_list(players[turn].cards)
    
    turn = turn + direction
    time.sleep(.5)

    #way to return to the starter of the round (will need to implement two way logic for reverse using if direction or abs())
    if turn == len(players) :
        turn = 0

    check_if_draw_pile_empty_then_shuffle(draw_pile,discard_pile)
    
    

print("Round over")








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