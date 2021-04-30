import random
from collections import Counter
class Card(object):
  def __init__(self,suit,value):
    self.suit = suit
    self.value = value

  def show(self):
    print(f"{self.value} of {self.suit}" )
  def __repr__(self):
    return f'{self.value} of {self.suit}'  
        

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
    self.deck = Deck()
    self.deck.shuffle()

  def draw(self, num_cards):
    #create deck object, shuffle deck, draws specific number of cards
        
    for i in range(num_cards):
      self.hand.append(self.deck.draw())
        
    return self

  def showhand(self):
    card_list = []
    print(self.hand)
          
  def discard(self):
    print(f' You hold {self.hand}')
    num_cards = int(input('How many cards would you like to discard?'))
        
    while num_cards>0:
      
      string_hand = []
      for x in self.hand:
        y = str(x)
        string_hand.append(y)
    
      lst = enumerate(string_hand)
      
      print(f'You currently hold {self.hand}')
      card = input("Which card would you like to discard?")
      for x in lst:
        if card == x[1]:
          del self.hand[x[0]]
                    
          num_cards-=1     
        
    return self.hand

  def five_card_draw(self):
        
    for i in range(3):
      length = len(self.hand)
      player.draw(5-length)
      player.discard()
    
    length = len(self.hand)
    player.draw(5-length)
    
    return self.hand  
  
  def rank_hand(self):
  
    string_hand = []
    for x in self.hand:
      y = str(x)
      y = y.replace("of","")
      y = y.split(' ')
      del y[1]
      string_hand.append(y)

    nums = []    
    suits = set()
    #Check for flush
    for x in string_hand:
      suits.add(x[1])
      nums.append(x[0])
    
    Flush = False
    if len(suits)==1:
    #check for flush
      Flush = True
    
       
    num_counts = Counter(nums)    
    max_count = max(num_counts.values())
    counter = 0
        
    high_cards = []
        
    Conversion_Dict = {'Ace':14, 'King':13, 'Queen':12, 'Jack':11 }
    cards = []
    
    if max_count == 1:
      for key in num_counts.keys():
        cards.append(key)
    card_values = []

    if len(cards)>0:

      for x in cards:
        if x in Conversion_Dict.keys():
          card_values.append(Conversion_Dict[x])
        else:
          card_values.append(int(x))

    if len(card_values)>0:
      max_card = max(card_values)
      
      if max_card>10:
        for k,v in Conversion_Dict.items():
          if max_card == v:
            True_Max = k
      elif max_card<=10:
        True_Max = max_card
      
      if Flush == True:
        return f'{True_Max} high flush!'
      if Flush == False:
        return f'{True_Max} high'  

    #Check for straight
    if len(card_values)>0:

      if max(card_values)-min(card_values)==len(card_values)-1:
        if Flush == True:
          return f'{True_Max} high straight flush'
        if Flush == False:
          return f'{True_Max} high straight'  
    

                  



      

       
    


player = Player('Jesse')
player.five_card_draw()

player.showhand()
print(player.rank_hand())
#TODO create function that identifies player's hand, pair, full house, straight, etc

