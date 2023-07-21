import random

class Card:
    def __innit__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print('{} of {}'.format(self.vaule, self.suit))

    def realVal(self):
        if self.value == 11:
            return 11
        if self.value == 12:
            return 12
        if self.value == 13:
            return 13
        if self.value == 14:
            return 14
        return self.value
        


class Deck:
    def __innit__(self):
        self.cards = []
        self.build()

def build(self):
    for s in ["Spades", "Clubs", "Hearts", "Diamonds"]:
        for v in range(2,14):
            self.cards.append(Card(s, v))

def show(self):
    for c in self.cards:
        c.show()

def shuffle(self):
    random.shuffle(self.cards)

def drawCard(self):
    return self.cards.pop()


class Player:
    def __innit__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self
    
    def countCards(self):
        sum = 0






deck = Deck()
deck.shuffle()
player1= Player('Shaq')
player2 = Player('Kobe') 
player1.draw(deck)
player2.draw(deck)       





# import random
# ranks=[2,3,4,5,6,7,8,9,10,'J','K','A','Q']
# design =['H','D','S','C']

# class Deck:
#     def __init__(self):
#         print("Creating new ordered deck!!")
#         self.cards=[(j,i) for j in design for i in ranks]
#     def shuffle(self):
#         print("Shuffling Deck")
#         random.shuffle(self.cards)
#     def split_half(self):
#         return (self.cards[:26],self.cards[26:]) 

# class Hand:
#     def __init__(self,cards_count):
#          self.cards_count=cards_count
#     def __str__(self):
#         return "Contains {} cards".format(len(self.cards_count))
#     def add(self,added_cards):
#         self.cards_count.extend(added_cards)
#     def remove(self):
#         return self.cards_count.pop()
# class Player:
#     def __init__(self,name,hand):
#         self.name=name
#         self.hand=hand
#     def play_card(self):
#         drawn_card = self.hand.remove()
#         print("{} has placed : {}".format(self.name,drawn_card))
#         print("\n")
#         return drawn_card
#     def remove_war_cards(self):
#         war_cards=[]
#         if len(self.hand.cards_count)<3:
#             return self.hand.cards_count
#         else:
#             for x in range(3):
#                 war_cards.append(self.hand.cards_count.pop())
#             return war_cards
#     def still_has_cards(self):
#         return len(self.hand.cards_count) != 0
# print("Welcome to War, Let's run into our game...")
# d= Deck()
# d.shuffle()
# half1,half2=d.split_half()

# comp = Player("Computer",Hand(half1))
# name=input("Enter your name")
# human = Player(name,Hand(half2))

# total_rounds =0
# war_count = 0

# while human.still_has_cards() and comp.still_has_cards():
#     total_rounds += 1
#     print("Time for a new round")
#     print("Here are the current standings")
#     print(human.name + "has the count:"+str(len(human.hand.cards_count)))
#     print(comp.name + "has the count:"+str(len(comp.hand.cards_count)))
#     print("Play a card!")
#     print("\n")

#     table_cards = []

#     c_card = comp.play_card()
#     p_card = human.play_card()
#     table_cards.append(c_card)
#     table_cards.append(p_card)

#     if c_card[1] == p_card[1]:
#         war_count += 1
#         print("War!!")
#         table_cards.extend(human.remove_war_cards())
#         table_cards.extend(comp.remove_war_cards())

#         if ranks.index(c_card[1]) < ranks.index(p_card[1]):
#             human.hand.add(table_cards)
#         else:
#             comp.hand.add(table_cards)
#     else:
#         if ranks.index(c_card[1]) < ranks.index(p_card[1]):
#             human.hand.add(table_cards)
#         else:
#             comp.hand.add(table_cards)
# print("Game over,number of rounds:"+str(total_rounds))
# print("A war happened " + str(war_count) +" times")
# print("Does the computer still have cards?\t",str(comp.still_has_cards()))
# print("Does the player still have cards?\t:",str(human.still_has_cards()))