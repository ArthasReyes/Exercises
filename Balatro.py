class Balatro:
    def __init__(self):
        self.state = "menu"
        self.deck = []
        self.hand = []

    def loop(self):
        while True:
            if self.state == "menu":
                self.menu()
            elif self.state == "demo":
                self.demo()

    def menu(self):
        option = input('''
1. Nueva baraja
2. Mostrar baraja
3. Barajar
4. Jugar Demo 
##########################             
''')
        if option == '1':
            self.new_deck()
        elif option == '2':
            self.show_deck()
        elif option == '3':
            self.shuffle_deck()
        elif option == '4':
            self.state = "demo"
        else:
            print("Opción no válida.")

    def demo(self):
        win_conditions = {
            'chips': 500,
            'hand_remaining': 3,
            'cards_on_hand': 9,
            'max_cards_to_play': 5,
        }
            
        posible_chips = {
            'high_card': {'chips': 1, 'multiply_by':1},
            'pair': {'chips': 2, 'multiply_by':1},
            'two_pairs': {'chips': 3, 'multiply_by':1},
            'three_of_a_kind': {'chips': 4, 'multiply_by':1},
            'straight': {'chips': 5, 'multiply_by':1},
            'flush': {'chips': 6, 'multiply_by':1},
            'full_house': {'chips': 7, 'multiply_by':1},
            'four_of_a_kind': {'chips': 8, 'multiply_by':1},
            'straight_flush': {'chips': 9, 'multiply_by':1},
        }
        self.new_deck()
        self.shuffle_deck()
        self.get_hand(win_conditions['cards_on_hand'])
        self.show_hand()
        
        selected_cards = []
        while not self.selected_cards_validation(selected_cards):
            selected_cards = input('''Para botar cartas:
seleccione posición de cartas de la forma 011101110
1 para seleccionar, 0 para no seleccionar: ''')
        self.drop_cards(selected_cards)

        selected_cards = []
        while not self.selected_cards_validation(selected_cards):
            selected_cards = input('''Para jugar la mano:
seleccione posición de cartas de la forma 011101110
1 para seleccionar, 0 para no seleccionar, máximo 5 1's: ''')
            
        best_chips = 0
        chips = 0
        best_hand = None        
        if self.has_high_card(selected_cards):
            hand = self.get_high_card(selected_cards)
            chips = self.calculate_chips(posible_chips['high_card'])
            if chips > best_chips:
                best_chips = chips
                best_hand = hand
        if self.has_pair(selected_cards):
            hand = self.get_pair(selected_cards)
            chips = self.calculate_chips(posible_chips['pair'])
            if chips > best_chips:
                best_chips = chips
                best_hand = hand
        if self.has_two_pairs(selected_cards):
            hand = self.get_two_pairs(selected_cards)
            chips = self.calculate_chips(posible_chips['two_pairs'])
            if chips > best_chips:
                best_chips = chips
                best_hand = hand
        if self.has_three_of_a_kind(selected_cards):
            hand = self.get_three_of_a_kind(selected_cards)
            chips = self.calculate_chips(posible_chips['three_of_a_kind'])
            if chips > best_chips:
                best_chips = chips
                best_hand = hand
        if self.has_straight(selected_cards):
            hand = self.get_straight(selected_cards)
            chips = self.calculate_chips(posible_chips['straight'])
            if chips > best_chips:
                best_chips = chips
                best_hand = hand
        if self.has_flush(selected_cards):
            hand = self.get_flush(selected_cards)
            chips = self.calculate_chips(posible_chips['flush'])
            if chips > best_chips:
                best_chips = chips
                best_hand = hand
        if self.has_full_house(selected_cards):
            hand = self.get_full_house(selected_cards)
            chips = self.calculate_chips(posible_chips['full_house'])
            if chips > best_chips:
                best_chips = chips
                best_hand = hand
        if self.has_four_of_a_kind(selected_cards):
            hand = self.get_four_of_a_kind(selected_cards)
            chips = self.calculate_chips(posible_chips['four_of_a_kind'])
            if chips > best_chips:
                best_chips = chips
                best_hand = hand
        if self.has_straight_flush(selected_cards):
            hand = self.get_straight_flush(selected_cards)
            chips = self.calculate_chips(posible_chips['straight_flush'])
            if chips > best_chips:
                best_chips = chips
                best_hand = hand
        
        print(f"Mejor mano: {best_hand} con {best_chips} fichas.")
        "Ganaste la demo" if best_chips >= win_conditions['chips'] else "No ganaste la demo"

        self.state = "menu"

    def new_deck(self):
        pass

    def show_deck(self):
        pass

    def shuffle_deck(self):
        pass

    def get_hand(self, num_cards):
        pass

    def show_hand(self):
        pass

    def selected_cards_validation(self, selected_cards):
        pass

    def drop_cards(self, selected_cards):
        pass

    def has_high_card(self, selected_cards):
        return True

    def get_high_card(self, selected_cards):
        pass
    
    def has_pair(self, selected_cards):
        return True

    def get_pair(self, selected_cards):
        pass

    def calculate_chips(self, chips_info):
        return 0

    def has_two_pairs(self, selected_cards):
        return True

    def get_two_pairs(self, selected_cards):
        pass

    def has_three_of_a_kind(self, selected_cards):
        return True

    def get_three_of_a_kind(self, selected_cards):
        pass

    def has_straight(self, selected_cards):
        return True

    def get_straight(self, selected_cards):
        pass

    def has_flush(self, selected_cards):
        return True

    def get_flush(self, selected_cards):
        pass

    def has_full_house(self, selected_cards):
        return True

    def get_full_house(self, selected_cards):
        pass

    def has_four_of_a_kind(self, selected_cards):
        return True

    def get_four_of_a_kind(self, selected_cards):
        pass

    def has_straight_flush(self, selected_cards):
        return True

    def get_straight_flush(self, selected_cards):
        pass


def main():
    game = Balatro()
    game.loop()

def test():
    game = Balatro()
    game.new_deck()
    
    ############ new_deck tests
    another_deck = [('T', 1), ('T', 2), ('T', 3), ('T', 4), ('T', 5), ('T', 6), ('T', 7), ('T', 8), ('T', 9), ('T', 10), ('T', 11), ('T', 12), ('T', 13), ('C', 1), ('C', 2), ('C', 3), ('C', 4), ('C', 5), ('C', 6), ('C', 7), ('C', 8), ('C', 9), ('C', 10), ('C', 11), ('C', 12), ('C', 13), ('D', 1), ('D', 2), ('D', 3), ('D', 4), ('D', 5), ('D', 6), ('D', 7), ('D', 8), ('D', 9), ('D', 10), ('D', 11), ('D', 12), ('D', 13), ('P', 1), ('P', 2), ('P', 3), ('P', 4), ('P', 5), ('P', 6), ('P', 7), ('P', 8), ('P', 9), ('P', 10), ('P', 11), ('P', 12), ('P', 13)]
    assert game.deck == another_deck
    game.shuffle_deck()
    assert game.deck != another_deck
    game.get_hand(9)
    assert len(game.hand) == 9
    assert len(game.deck) == 43
    assert all(card not in game.deck for card in game.hand)
    game.drop_cards('000000011')
    assert len(game.hand) == 7
    game.get_hand(9)
    assert len(game.hand) == 9
    assert len(game.deck) == 41
    assert all(card not in game.deck for card in game.hand)
    
    ########### selected_cards_validation tests
    selected_cards = '111000001'
    assert game.selected_cards_validation(selected_cards) == True
    selected_cards = '111111001'
    assert game.selected_cards_validation(selected_cards) == False


    ############ has and get hand tests
    game.hand = [('P', 2), ('C', 2), ('P', 2), ('T', 2), ('P', 7), ('C', 4), ('P', 9), ('C', 13), ('D', 5)]
    
    selected_cards = '111110000'  
    assert game.has_high_card(selected_cards) == True
    assert game.get_high_card(selected_cards) == [('P', 7)]
    selected_cards = '010001110'  
    assert game.has_high_card(selected_cards) == True
    assert game.get_high_card(selected_cards) == [('C', 13)]
    
    selected_cards = '011000000'
    assert game.has_pair(selected_cards) == True
    assert game.get_pair(selected_cards) == [('C', 2), ('P', 2)]
    selected_cards = '001100011'
    assert game.has_pair(selected_cards) == True
    assert game.get_pair(selected_cards) == [('P', 2), ('T', 2)]



if __name__ == "__main__":
    test()
    main()
