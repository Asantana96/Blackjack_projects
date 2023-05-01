import random

class Blackjack:
    def __init__(self):
        self.playerIn = True
        self.dealerIn = True
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2,
                     3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 'Q', 'K', 'A', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
        self.playersHand = []
        self.dealerHand = []

    def dealCard(self, turn):
        card = random.choice(self.deck)
        turn.append(card)
        self.deck.remove(card)

    def total(self, turn):
        total = 0
        face = ['J', 'Q', 'K']
        for card in turn:
            if isinstance(card, int):
                total += card
            elif card in face:
                total += 10
            else:
                if total > 11:
                    total += 1
                else:
                    total += 11
        return total

    def revealDealerHand(self):
        if len(self.dealerHand) == 2:
            return self.dealerHand[0]
        elif len(self.dealerHand) > 2:
            return self.dealerHand[0], self.dealerHand[1]

    def driver(self):
        for i in range(2):
            self.dealCard(self.dealerHand)
            self.dealCard(self.playersHand)

        while self.playerIn or self.dealerIn:
            print(f'Dealer has {self.revealDealerHand()} and X')
            print(f'You have {self.playersHand} for a total of {self.total(self.playersHand)}')
            if self.playerIn:
                stayOrHit = input('1: Stay\n2: Hit\n')
                if stayOrHit == '1':
                    self.playerIn = False
                else:
                    self.dealCard(self.playersHand)
            if self.total(self.dealerHand) > 16:
                self.dealerIn = False
            else:
                self.dealCard(self.dealerHand)
            if self.total(self.playersHand) >= 21:
                break
            elif self.total(self.dealerHand) >= 21:
                break
            if self.total(self.playersHand) == 21:
                break

        print(f'\nYou have {self.playersHand} for a total of {self.total(self.playersHand)} and the dealer has {self.total(self.dealerHand)}')

        if self.total(self.playersHand) == 21:
            print("Blackjack! You win!")
        elif self.total(self.dealerHand) == 21:
            print("Blackjack! Dealer wins!")
        elif self.total(self.playersHand) > 21:
            print("you bust! Dealer wins")
        elif self.total(self.dealerHand) > 21:
            print("Dealer busts! You win!")
        elif 21 - self.total(self.dealerHand) < 21 - self.total(self.playersHand):
            print("Dealer Wins!")
        elif 21 - self.total(self.dealerHand) > 21 - self.total(self.playersHand):
            print('You win!')
game = Blackjack()
game.driver()

