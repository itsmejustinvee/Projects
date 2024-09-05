#importing the random module
import random

#making a class to represent the cards
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
    def value(self):
        if self.rank in ['Jack', 'Queen', 'King']:
            return 10
        elif self.rank == 'Ace':
            return 11
        else:
            return int(self.rank)
        

#making a class for the deck     
class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Deck.suits for rank in Deck.ranks]
        random.shuffle(self.cards)
        
    def deal_card(self):
        return self.cards.pop() if self.cards else None
    
    def remaining_cards(self):
        return len(self.cards)
      
#Making a class for the player 
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        
    def add_card(self, card):
        self.hand.append(card)
        
    def hand_value(self):
        value = sum(card.value() for card in self.hand)
        aces = sum(1 for card in self.hand if card.rank == 'Ace')
        #changing value of ace if its more than 21
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value
    
    def is_bust(self):
        return self.hand_value() > 21
    
    def __str__(self):
        return f'{self.name} has {[str(card) for card in self.hand]} with a total score of {self.hand_value()}'
    
#Game rules
def play_blackjack():
    deck = Deck()
    
    player1 = Player('Player 1')
    player2 = Player('Player 2')
    
    while deck.remaining_cards() > 0:
        player1.add_card(deck.deal_card())
        player2.add_card(deck.deal_card())
        
        print(player1)
        print(player2)
        
        #did any1 bust
        if player1.is_bust():
            print('Player 1 has busted, and has lost the game. GG!')
            break
        elif player2.is_bust():
            print('Player 2 has busted, and has lost the game. GG!')
            break
        
        input('Press Enter to deal the next card.')
        
    if not player1.is_bust() and not player2.is_bust():
        if player1.hand_value() > player2.hand_value():
            print('Player 1 is the reigning champion')
        elif player2.hand_value() > player1.hand_value():
            print('Player 2 wins!')
        else:
            print('Tie game, you both suck')
            
play_blackjack()

    
    