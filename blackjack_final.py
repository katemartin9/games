import random

class Card:
    def __init__(self,name,suit,score):
        self.name = name
        self.suit = suit
        self.score = score
    
    def __repr__(self):
        return f'{self.name} of {self.suit}'

def deck_of_cards():
    suits = ['clubs','diamonds','hearts','spades']
    cards = ['ace','two','three','four','five','six','seven','eight','nine','ten','jack','queen','king']
    deck_list = [Card(name=cards[card],suit=suits[suit],score=card+1) 
                 for card in range(len(cards)) for suit in range(len(suits))]
    random.shuffle(deck_list)
    return deck_list

    
class Blackjack:
    def __init__(self):
        self.name = None
        self.user_score = None
        self.dealer_score = None
        self.deck = deck_of_cards()
        self.dealer_hand = [self.deck.pop() for x in range(2)]
        self.player_hand = [self.deck.pop() for y in range(2)]

    def __repr__(self):
        return f'User Name: {self.name} \nUser Score: {self.user_score}'

    def score_calculating(self,any_hand):
        score = 0
        contains_ace = False
        for card in any_hand:
            if card.score > 10:
                score += 10
            else:
                score += card.score
            if card.name == 'ace':
                contains_ace = True
        if score < 12 and contains_ace:
            score += 10
        return score
    
    def player_choice(self):
        while True:
            user_choice = input("Hit or stand?")
            if user_choice[0].lower() == 'h':
                self.player_hand.append(self.deck.pop())
                new_score = self.score_calculating(self.player_hand)
                print(f'Your current score is {new_score}')
                if new_score == 21:
                    return
                elif new_score > 21:    
                    return f'{self.name} is BUST'
            else:
                return
    
    def dealer_choice(self):
        current_score = self.score_calculating(self.dealer_hand)
        while current_score < self.score_calculating(self.player_hand) and current_score < 21:
            self.dealer_hand.append(self.deck.pop())
            current_score = self.score_calculating(self.dealer_hand)
            if current_score > 21:
                print('Dealer went BUST. Player wins!')
                print(f"Dealer's score: {self.score_calculating(self.dealer_hand)}")
                return
        if current_score == self.score_calculating(self.player_hand):
            print('Draw!')
            return
        else: 
            print('Dealer wins')
            print(f"Dealer's score: {self.score_calculating(self.dealer_hand)}")  

    #next to self add in only those arguments that you pass in yourself not via input
    def game_on(self):
        self.name = input('Welcome to Blackjack! Please input your name: ')
        print(f"Your cards are: {self.player_hand[0]}, {self.player_hand[1]} \nDealer's hand: {self.dealer_hand[0]}")
        print(f"{self.name}'s score: {self.score_calculating(self.player_hand)}")
        print(f"Dealer's score: {self.score_calculating(self.dealer_hand)}")
        if self.player_hand == 21:
            print('Blackjack! Player wins!')
            return
    
        else:
            result = self.player_choice()
            if result:
                print(result)
                return
            if self.score_calculating(self.dealer_hand) == 17:
                if self.score_calculating(self.dealer_hand) > self.score_calculating(self.player_hand):
                    print('Dealer Wins!')
                    return
            self.dealer_choice()
                
if __name__ == "__main__":
    B = Blackjack()
    B.game_on()
