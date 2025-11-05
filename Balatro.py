from typing import List, Tuple
Card = Tuple[str, int]  # ('P', 2), ('C', 10), etc.

class Balatro:
    def __init__(self):
        self.state: str = "menu"
        self.deck: List[Card] = []
        self.hand: List[Card] = []

    def loop(self) -> None:
        while True:
            if self.state == "menu":
                self.menu()
            elif self.state == "demo":
                self.demo()

    def menu(self) -> None:
        option = input('''
1. Nueva baraja
2. Barajar
3. Jugar Demo 
##########################             
''')
        if option == '1':
            self.new_deck()
            self.show_deck()
        elif option == '2':
            self.shuffle_deck()
            self.show_deck()
        elif option == '3':
            self.state = "demo"
        else:
            print("Opción no válida.")

    def demo(self) -> None:
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
        
        cards_to_drop = ''
        while not self.droped_cards_validation(cards_to_drop):
            cards_to_drop = input('''Para botar cartas:
seleccione posición de cartas de la forma 011101110
1 para seleccionar, 0 para no seleccionar: ''')
        self.drop_cards(cards_to_drop)

        cards_to_play = ''
        while not self.selected_cards_validation(cards_to_play):
            cards_to_play = input('''Para jugar la mano:
seleccione posición de cartas de la forma 011101110
1 para seleccionar, 0 para no seleccionar, máximo 5 1's: ''')
            
        best_chips = 0
        chips = 0
        best_hand = None        
        if self.has_high_card(cards_to_play):
            hand = self.get_high_card(cards_to_play)
            chips = self.calculate_chips(posible_chips['high_card'])
            if chips > best_chips:
                best_chips = chips
                best_hand = hand
        if self.has_pair(cards_to_play):
            hand = self.get_pair(cards_to_play)
            chips = self.calculate_chips(posible_chips['pair'])
            if chips > best_chips:
                best_chips = chips
                best_hand = hand
        if self.has_two_pairs(cards_to_play):
            hand = self.get_two_pairs(cards_to_play)
            chips = self.calculate_chips(posible_chips['two_pairs'])
            if chips > best_chips:
                best_chips = chips
                best_hand = hand
        if self.has_three_of_a_kind(cards_to_play):
            hand = self.get_three_of_a_kind(cards_to_play)
            chips = self.calculate_chips(posible_chips['three_of_a_kind'])
            if chips > best_chips:
                best_chips = chips
                best_hand = hand
        if self.has_straight(cards_to_play):
            hand = self.get_straight(cards_to_play)
            chips = self.calculate_chips(posible_chips['straight'])
            if chips > best_chips:
                best_chips = chips
                best_hand = hand
        if self.has_flush(cards_to_play):
            hand = self.get_flush(cards_to_play)
            chips = self.calculate_chips(posible_chips['flush'])
            if chips > best_chips:
                best_chips = chips
                best_hand = hand
        if self.has_full_house(cards_to_play):
            hand = self.get_full_house(cards_to_play)
            chips = self.calculate_chips(posible_chips['full_house'])
            if chips > best_chips:
                best_chips = chips
                best_hand = hand
        if self.has_four_of_a_kind(cards_to_play):
            hand = self.get_four_of_a_kind(cards_to_play)
            chips = self.calculate_chips(posible_chips['four_of_a_kind'])
            if chips > best_chips:
                best_chips = chips
                best_hand = hand
        if self.has_straight_flush(cards_to_play):
            hand = self.get_straight_flush(cards_to_play)
            chips = self.calculate_chips(posible_chips['straight_flush'])
            if chips > best_chips:
                best_chips = chips
                best_hand = hand
        
        print(f"Mejor mano: {best_hand} con {best_chips} fichas.")
        # TODO: imprimir resultado de victoria o derrota
        print("Ganaste la demo") if best_chips >= win_conditions['chips'] else print("No ganaste la demo")

        self.state = "menu"

    def new_deck(self) -> None:
        # TODO: Crear las 52 cartas como lista de tuplas (palo, valor)
        # palos: 'T', 'C', 'D', 'P'
        pass

    def show_deck(self) -> None:
        # TODO: Imprimir la baraja actual en pantalla
        pass

    def shuffle_deck(self) -> None:
        # TODO: Mezclar la baraja
        pass

    def get_hand(self, num_cards: int) -> None:
        # TODO: Rellenar la mano hasta tener 'num_cards' cartas
        # tomar las cartas necesarias desde self.deck
        pass

    def show_hand(self) -> None:
        # TODO: Mostrar la mano actual con índices (para selección)
        pass

    def selected_cards_validation(self, selected_cards: str) -> bool:
        # TODO: retornar True si la cadena tiene 9 caracteres (0/1)
        # TODO: validar máximo de 5 "1" cuando sea jugada
        return False
    
    def droped_cards_validation(self, selected_cards: str) -> bool:
        # TODO: retornar True si la cadena tiene 9 caracteres (0/1)
        return False
    
    def drop_cards(self, selected_cards: str) -> None:
        # TODO: Eliminar de self.hand las cartas marcadas con '1'
        pass

    def has_high_card(self, selected_cards: str) -> bool:
        # TODO: retornar True si hay carta alta válida
        return False

    def get_high_card(self, selected_cards: str) -> List[Card]:
        # TODO: devolver la carta más alta entre las seleccionadas
        return []
    
    def has_pair(self, selected_cards: str) -> bool:
        # TODO: retornar True si hay par entre las seleccionadas
        return False

    def get_pair(self, selected_cards: str) -> List[Card]:
        # TODO: devolver las cartas del par
        return []

    def calculate_chips(self, chips_info: dict) -> int:
        # TODO: calcular fichas según 'chips' y 'multiply_by'
        return 0

    def has_two_pairs(self, selected_cards: str) -> bool:
        # TODO: detectar dos pares
        return False

    def get_two_pairs(self, selected_cards: str) -> List[Card]:
        # TODO: devolver las cartas de ambos pares
        return []

    def has_three_of_a_kind(self, selected_cards: str) -> bool:
        # TODO: detectar trío
        return False

    def get_three_of_a_kind(self, selected_cards: str) -> List[Card]:
        # TODO: devolver las tres cartas iguales
        return []

    def has_straight(self, selected_cards: str) -> bool:
        # TODO: detectar escalera
        return False

    def get_straight(self, selected_cards: str) -> List[Card]:
        # TODO: devolver las cartas consecutivas
        return []

    def has_flush(self, selected_cards: str) -> bool:
        # TODO: detectar color
        return False

    def get_flush(self, selected_cards: str) -> List[Card]:
        # TODO: devolver las cartas del mismo palo
        return []

    def has_full_house(self, selected_cards: str) -> bool:
        # TODO: detectar full house
        return False

    def get_full_house(self, selected_cards: str) -> List[Card]:
        # TODO: devolver las cartas del full
        return []

    def has_four_of_a_kind(self, selected_cards: str) -> bool:
        # TODO: detectar póker
        return False

    def get_four_of_a_kind(self, selected_cards: str) -> List[Card]:
        # TODO: devolver las cuatro cartas iguales
        return []

    def has_straight_flush(self, selected_cards: str) -> bool:
        # TODO: detectar escalera de color
        return False

    def get_straight_flush(self, selected_cards: str) -> List[Card]:
        # TODO: devolver las cartas de la escalera de color
        return []


def main() -> None:
    new_deck_test()
    selected_cards_validation_tests()
    has_and_get_hand_tests()
    win_conditions_tests()
    game = Balatro()
    game.loop()


def new_deck_test() -> None:
    game = Balatro()
    game.new_deck()
    
    another_deck = [('T', 1), ('T', 2), ('T', 3), ('T', 4), ('T', 5), ('T', 6), ('T', 7), ('T', 8), ('T', 9), ('T', 10), ('T', 11), ('T', 12), ('T', 13),
                    ('C', 1), ('C', 2), ('C', 3), ('C', 4), ('C', 5), ('C', 6), ('C', 7), ('C', 8), ('C', 9), ('C', 10), ('C', 11), ('C', 12), ('C', 13),
                    ('D', 1), ('D', 2), ('D', 3), ('D', 4), ('D', 5), ('D', 6), ('D', 7), ('D', 8), ('D', 9), ('D', 10), ('D', 11), ('D', 12), ('D', 13),
                    ('P', 1), ('P', 2), ('P', 3), ('P', 4), ('P', 5), ('P', 6), ('P', 7), ('P', 8), ('P', 9), ('P', 10), ('P', 11), ('P', 12), ('P', 13)]
    assert game.deck == another_deck
    game.shuffle_deck()
    assert game.deck != another_deck
    game.get_hand(9)
    assert len(game.hand) == 9
    assert len(game.deck) == 43
    assert all(card not in game.deck for card in game.hand)
    game.drop_cards('000000011')
    assert len(game.hand) == 9  # Se repone hasta tener 9
    assert len(game.deck) == 43 - 2
    assert all(card not in game.deck for card in game.hand)
    
def selected_cards_validation_tests() -> None:
    game = Balatro()
    selected_cards = '111000001'
    assert game.selected_cards_validation(selected_cards) == True
    selected_cards = '111111001'
    assert game.selected_cards_validation(selected_cards) == False
    selected_cards = '111000001001'
    assert game.selected_cards_validation(selected_cards) == False
    
    selected_cards = '111111111'
    assert game.droped_cards_validation(selected_cards) == True
    selected_cards = '11111111111'
    assert game.droped_cards_validation(selected_cards) == False


def has_and_get_hand_tests() -> None:
    game = Balatro()
    game.hand = [('P', 2), ('C', 2), ('P', 2), ('T', 2), ('P', 7), ('C', 4), ('P', 9), ('C', 13), ('D', 5)]
    #high card tests
    selected_cards = '111110000'  
    assert game.has_high_card(selected_cards) == True
    assert game.get_high_card(selected_cards) == [('P', 7)]
    selected_cards = '010001110'  
    assert game.has_high_card(selected_cards) == True
    assert game.get_high_card(selected_cards) == [('C', 13)]
    
    #pair tests
    selected_cards = '011000000'
    assert game.has_pair(selected_cards) == True
    assert game.get_pair(selected_cards) == [('C', 2), ('P', 2)]
    selected_cards = '001100011'
    assert game.has_pair(selected_cards) == True
    assert game.get_pair(selected_cards) == [('P', 2), ('T', 2)]

    # TODO: implementar tests para dos pares, trío, escalera, color, full house, póker y escalera de color

def win_conditions_tests() -> None:
    # TODO: definir condiciones de victoria o empate para probar
    pass


if __name__ == "__main__":
    main()
