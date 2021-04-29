import random 
class Card(object):
  def __init__(self,suit,value):
    self.suit = suit
    self.value = value

  def show(self):
    print(f"{self.value} of {self.suit}" )
        

class Deck(object):
  def __init__(self):
    self.cards = []
    self.build()

  def build(self):
    numbers = [2,3,4,5,6,7,8,9,10,'Jack', 'Queen', 'King', 'Ace']
    for i in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
      for x in numbers:
        #adding Card Class objects inside of this Deck object
        self.cards.append(Card(i,x))
  def show(self):
    for x in self.cards:
      #using card's show method inside of this deck method, for each card
      x.show()
    print(len(self.cards))
  def shuffle(self):
    for x in range(len(self.cards)-1, 0, -1):
      rand = random.randint(0, x)
      self.cards[x], self.cards[rand] = self.cards[rand], self.cards[x] 
  def draw(self):
    return self.cards.pop()

class Player(object):
  def __init__(self, name):
    self.hand = []
    self.name = name
  def draw(self, deck):
    self.hand.append(deck.draw())
    return self
  def showhand(self):
    card_list = []
    for card in self.hand:
      card.show()
          
  def discard(self):
    player.showhand()


deck = Deck()
deck.shuffle()
player = Player('Jesse')

for i in range(5):
  a = player.draw(deck)

a.showhand()

