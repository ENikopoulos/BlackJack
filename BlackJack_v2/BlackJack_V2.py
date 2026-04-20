import tkinter as tk
import random

# --- Game Logic ---

suits = ("Hearts","Clubs","Diamonds","Spades")
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(s, r) for s in suits for r in ranks]
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) < 10:
            self.__init__()  # reshuffle
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1
        self.adjust_for_ace()

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def is_blackjack(self):
        return self.value == 21 and len(self.cards) == 2

    def is_bust(self):
        return self.value > 21

# --- GUI ---

class BlackjackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack")

        self.balance = 100
        self.bet = 10
        self.game_over = False

        # Labels
        self.info = tk.Label(root, text="Welcome to Blackjack", font=("Arial", 14))
        self.info.pack()

        self.balance_label = tk.Label(root, text=f"Balance: ${self.balance}")
        self.balance_label.pack()

        self.player_label = tk.Label(root, text="Player: ")
        self.player_label.pack()

        self.dealer_label = tk.Label(root, text="Dealer: ")
        self.dealer_label.pack()

        # Buttons
        self.hit_btn = tk.Button(root, text="Hit", command=self.hit)
        self.hit_btn.pack(side=tk.LEFT, padx=10)

        self.stand_btn = tk.Button(root, text="Stand", command=self.stand)
        self.stand_btn.pack(side=tk.LEFT, padx=10)

        self.new_btn = tk.Button(root, text="New Round", command=self.new_round)
        self.new_btn.pack(side=tk.LEFT, padx=10)

        self.new_round()

    def update_display(self, hide_dealer=True):
        player_cards = ', '.join(str(c) for c in self.player_hand.cards)

        if hide_dealer and not self.game_over:
            dealer_cards = f"{self.dealer_hand.cards[0]}, [Hidden]"
        else:
            dealer_cards = ', '.join(str(c) for c in self.dealer_hand.cards)

        self.player_label.config(text=f"Player ({self.player_hand.value}): {player_cards}")
        self.dealer_label.config(text=f"Dealer ({self.dealer_hand.value if self.game_over else '?'}): {dealer_cards}")
        self.balance_label.config(text=f"Balance: ${self.balance}")

    def end_round(self, message, payout=0):
        self.info.config(text=message)
        self.balance += payout
        self.game_over = True
        self.update_display(hide_dealer=False)

    def new_round(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.game_over = False

        # Deal
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())

        # Check blackjack
        if self.player_hand.is_blackjack():
            if self.dealer_hand.is_blackjack():
                self.end_round("Push! Both have Blackjack.", 0)
            else:
                self.end_round("Blackjack! You win 3:2!", int(self.bet * 1.5))
        else:
            self.info.config(text="Your move")

        self.update_display()

    def hit(self):
        if self.game_over:
            return

        self.player_hand.add_card(self.deck.deal())
        self.update_display()

        if self.player_hand.is_bust():
            self.end_round("Bust! Dealer wins.", -self.bet)

    def stand(self):
        if self.game_over:
            return

        # Dealer plays
        while self.dealer_hand.value < 17:
            self.dealer_hand.add_card(self.deck.deal())

        # Determine winner
        if self.dealer_hand.is_bust():
            self.end_round("Dealer busts! You win!", self.bet)
        elif self.dealer_hand.value > self.player_hand.value:
            self.end_round("Dealer wins!", -self.bet)
        elif self.dealer_hand.value < self.player_hand.value:
            self.end_round("You win!", self.bet)
        else:
            self.end_round("Push!", 0)

# --- Run ---

if __name__ == "__main__":
    root = tk.Tk()
    game = BlackjackGUI(root)
    root.mainloop()
