import pytest
from balatro import Balatro

############## Fixtures #############

@pytest.fixture
def game() -> Balatro:
    return Balatro()


@pytest.fixture
def basic_hand_game() -> Balatro:
    game = Balatro()
    game.hand = [
        ('P', 2), ('C', 2), ('P', 2), ('T', 2),
        ('P', 7), ('C', 4), ('P', 9), ('C', 13), ('D', 5)
    ]
    return game


@pytest.fixture
def intermediate_hand_game() -> Balatro:
    game = Balatro()
    game.hand = [
        ('P', 2), ('C', 2), ('P', 3), ('T', 2),
        ('P', 5), ('C', 4), ('P', 6), ('P', 13), ('D', 5)
    ]
    return game


@pytest.fixture
def advanced_hand_game() -> Balatro:
    game = Balatro()
    game.hand = [
        ('P', 2), ('C', 2), ('P', 3), ('T', 2),
        ('P', 5), ('C', 4), ('D', 2), ('P', 1), ('P', 4)
    ]
    return game

############# DECK ###################

def test_new_deck_creation(game: Balatro) -> None:
    game.new_deck()
    assert len(game.deck) == 52
    assert len(set(game.deck)) == 52


def test_shuffle_preserves_cards(game: Balatro) -> None:
    game.new_deck()
    original_deck = game.deck.copy()
    game.shuffle_deck()
    assert set(game.deck) == set(original_deck)

############ MANO Y DESCARTE ################

def test_get_hand_reduces_deck(game: Balatro) -> None:
    game.new_deck()
    game.shuffle_deck()
    game.get_hand(9)
    assert len(game.hand) == 9
    assert len(game.deck) == 43


def test_drop_cards_and_refill(game: Balatro) -> None:
    game.new_deck()
    game.shuffle_deck()
    game.get_hand(9)

    game.drop_cards('000000011')
    assert len(game.hand) == 7

    game.get_hand(9)
    assert len(game.hand) == 9

################ VALIDACIONES ####################

@pytest.mark.parametrize(
    "selected, expected",
    [
        ('111000001', True),
        ('111111001', False),
        ('111000001001', False),
    ]
)
def test_selected_cards_validation(game, selected, expected):
    assert game.selected_cards_validation(selected) is expected


@pytest.mark.parametrize(
    "selected, expected",
    [
        ('111111111', True),
        ('11111111111', False),
    ]
)
def test_droped_cards_validation(game, selected, expected):
    assert game.droped_cards_validation(selected) is expected


############## HIGH CARD #####################

def test_has_high_card(basic_hand_game):
    assert basic_hand_game.has_high_card('111110000') == True
    assert basic_hand_game.has_high_card('010001110') == True


def test_get_high_card(basic_hand_game):
    assert basic_hand_game.get_high_card('111110000') == [('P', 7)]
    assert basic_hand_game.get_high_card('010001110') == [('C', 13)]


################  Pair / Two Pair / Trio ############

def test_has_pair(basic_hand_game):
    assert basic_hand_game.has_pair('011000000') == True
    assert basic_hand_game.has_pair('001100011') == True

def test_has_pair_negative(basic_hand_game):
    assert basic_hand_game.has_pair('100010000') == False

def test_get_pair(basic_hand_game):
    assert basic_hand_game.get_pair('011000000') == [('C', 2), ('P', 2)]
    assert basic_hand_game.get_pair('001100011') == [('P', 2), ('T', 2)]

def test_has_two_pairs(basic_hand_game):
    assert basic_hand_game.has_two_pairs('111100000') == True

def test_has_two_pairs_negative(basic_hand_game):
    assert basic_hand_game.has_two_pairs('110011000') == False

def test_get_two_pairs(basic_hand_game):
    assert basic_hand_game.get_two_pairs('111100000') == [('C', 2), ('P', 2), ('T', 2), ('P', 2)]

def test_has_three_of_a_kind(basic_hand_game):
    assert basic_hand_game.has_three_of_a_kind('110100000') == True

def test_has_three_of_a_kind_negative(basic_hand_game):
    assert basic_hand_game.has_three_of_a_kind('110010000') == False

def test_get_three_of_a_kind(basic_hand_game):
    assert basic_hand_game.get_three_of_a_kind('110100000') == [('C', 2), ('P', 2), ('T', 2)]


#################### Straight / Flush / Full House #################

def test_has_straight(intermediate_hand_game):
    assert intermediate_hand_game.has_straight('101001101') == True

def test_has_straight_negative(intermediate_hand_game):
    assert intermediate_hand_game.has_straight('101001100') == False

def test_get_straight(intermediate_hand_game):
    assert intermediate_hand_game.get_straight('101001101') == [('P', 2), ('P', 3), ('C', 4), ('D', 5), ('P', 6)]

def test_has_flush(intermediate_hand_game):
    assert intermediate_hand_game.has_flush('101010110') == True

def test_has_flush_negative(intermediate_hand_game):
    assert intermediate_hand_game.has_flush('101011010') == False

def test_get_flush(intermediate_hand_game):
    assert intermediate_hand_game.get_flush('101010110') == [('P', 2), ('P', 3), ('P', 5), ('P', 6), ('P', 13)]

def test_has_full_house(intermediate_hand_game):
    assert intermediate_hand_game.has_full_house('110110001') == True

def test_has_full_house_negative(intermediate_hand_game):
    assert intermediate_hand_game.has_full_house('110101000') == False

def test_get_full_house(intermediate_hand_game):
    assert intermediate_hand_game.get_full_house('110110001') == [('P', 2), ('C', 2), ('T', 2), ('P', 5), ('D', 5)]

################### Four of a Kind / Straight Flush ############

def test_has_four_of_a_kind(advanced_hand_game):
    assert advanced_hand_game.has_four_of_a_kind('110100100') == True

def test_has_four_of_a_kind_negative(advanced_hand_game):
    assert advanced_hand_game.has_four_of_a_kind('110100000') == False

def test_get_four_of_a_kind(advanced_hand_game):
    assert advanced_hand_game.get_four_of_a_kind('110100100') == [('P', 2), ('C', 2), ('T', 2), ('D', 2)]

def test_has_straight_flush(advanced_hand_game):
    assert advanced_hand_game.has_straight_flush('101010011') == True

def test_has_straight_flush_negative(advanced_hand_game):
    assert advanced_hand_game.has_straight_flush('101000011') == False

def test_get_straight_flush(advanced_hand_game):
    assert advanced_hand_game.get_straight_flush('101010011') == [('P', 1), ('P', 2), ('P', 3), ('P', 4), ('P', 5)]

