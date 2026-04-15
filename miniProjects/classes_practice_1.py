class Players :
    initial_card_count = 4
    player_count = 1
    
    def __init__(self, name, card_count):
        Players.player_count += 1

        self.name = name
        self.card_count = card_count
        self.player_num = Players.player_count      
        self.player_code = name + '_' + str(self.player_num)

    def add_card(self, num_added_cards) :
        self.card_count = self.card_count + num_added_cards
        

    
player_1 = Players('Ali', Players.initial_card_count)
player_2 = Players('Othmane', Players.initial_card_count)

print(player_1.player_code)
print(player_2.player_code)



