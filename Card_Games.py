import random
from collections import Counter
import json


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
    self.Conversion_Dict = {'Ace':14, 'King':13, 'Queen':12, 'Jack':11 }
    self.Chips = self.load_chips()
    self.Reward_Dict = {"pair of Jacks": 1, "pair of Queens": 1, "pair of Kings": 1, "pair of Aces":1,\
      "two pair":2, "Three of a kind":4, "Full House":10, "4 of a kind":15, "high flush":8,
      "high straight": 7, "straight flush": 20, "Royal flush": 50
      }
    
  def load_chips(self):
    with open('Chips.json') as json_file:
      chips = json.load(json_file)
    
    for k,v in chips.items():
      if k == self.name:
        return v
      else:
        chips[self.name]=1000000
        with open('Chips.json', 'w') as outfile:
          json.dump(chips, outfile)
        return 1000000  
  
  def save_chips(self):

    with open('Chips.json') as json_file:
      chips = json.load(json_file)

      for k,v in chips.items():
        if k == self.name:
          
          chips[k]=self.Chips
          print(chips)
    with open('Chips.json', 'w') as outfile:
      json.dump(chips, outfile)
       


  def draw(self, num_cards):
    #create deck object, shuffle deck, draws specific number of cards
        
    for i in range(num_cards):
      self.hand.append(self.deck.draw())
        
    return self.hand 
  def bet(self):

    print(f'You currently have {self.Chips} dollars')
    variable = False
    while variable == False:
      is_decimal = False
      while is_decimal == False:
        wager = (input('How much would you like to bet this round?'))
        if wager.isdecimal() == True:
          is_decimal = True
      wager = int(wager)
      if wager <= self.Chips:
        variable = True
      self.Chips -= wager   
    print(f'You have bet {wager} chips')     
    return wager    

  def showhand(self):
    card_list = []
    print(self.hand)
          
  def discard(self):
    print(f' You hold {self.hand}')
    length = len(self.hand)
    lengths = []
    for i in range(length):
      lengths.append(i)

    variable = False
    while variable == False:
      is_decimal = False
      while is_decimal == False:
        num_cards = input('How many cards would you like to discard?')
        if num_cards.isdecimal() == True:
          is_decimal = True

      num_cards = int(num_cards)
      if num_cards in lengths:
        variable = True
           
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
    bet_total = 0
    
    self.draw(5)
    self.showhand()
    wager = self.bet()
    bet_total += wager
    self.discard()

    
    for i in range(2):
      length = len(self.hand)
      self.draw(5-length)
      self.discard()

    length = len(self.hand)            
    self.draw(5-length)
    print(self.hand)

    multiplier = self.evaluate_bet()
    
    if multiplier == 0:
      print(f'You lose {bet_total} chips. You have {self.Chips} chips remaining.')
      self.save_chips()
      return 
    
    final_return = multiplier * bet_total
    self.Chips += final_return
    print(f'Your hand was {self.rank_hand()}, you currently have {self.Chips} Chips remaining!')

    self.save_chips()
    
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
        
    value_counts = []
    for x in num_counts.values():
      value_counts.append(x)
    value_counts.sort()
    value_string = []
    for x in value_counts:
      y = str(x)
      value_string.append(y)

    value_join = ''.join(value_string)
      
    key_dictionary = {1112:'pair', 122:'two pair', 113: 'three of a kind',\
      23: 'full house', 14: '4 of a kind'}
    
    for k,v in key_dictionary.items():
      if int(value_join) == k:

        if v == 'pair':
          for k,v in num_counts.items():
            if v == max_count:
              return(f"pair of {k}s")
              
        if v == 'two pair':
          two_pair = []
          for k,v in num_counts.items():
            if v == max_count:
              two_pair.append(k)
          two_pair.sort()
          return(f"two pair {two_pair[1]}s and {two_pair[0]}s")
          
        if v == 'three of a kind':
          for k,v in num_counts.items():
            if v == max_count:
              return(f"Three of a kind {k}s")
              
        if v == 'full house':
          full_house_list = []
          for k,v in num_counts.items():
            if v == 2:
              full_house_list.append(k)
            if v == 3:
              full_house_list.append(k)
          return(f"Full House {full_house_list[0]}s and {full_house_list[1]}s")
          
        if v == '4 of a kind':
          for k,v in num_counts.items():
            if v == max_count:
              return(f"4 of a kind {k}s")
              
    cards = []
    
    if max_count == 1:
      #checking for non pairs
      for key in num_counts.keys():
        cards.append(key)
    card_values = []

    if len(cards)>0:

      for x in cards:
        if x in self.Conversion_Dict.keys():
          card_values.append(self.Conversion_Dict[x])
        else:
          card_values.append(int(x))

    if len(card_values)>0:
      max_card = max(card_values)
      
      if max_card>10:
        for k,v in self.Conversion_Dict.items():
          if max_card == v:
            True_Max = k
      elif max_card<=10:
        True_Max = max_card
      
      if max(card_values)-min(card_values)==len(card_values)-1:
        #Checking for straight, applying flush or non flush to straight
        if Flush == True:
          if max_card == 14:
            return(f'Royal flush!')
            
          else:
            return(f'{True_Max} high straight flush')
            
        if Flush == False:
          return(f'{True_Max} high straight')  
               
      #Applying Flush or Non Flush 
      if Flush == True:
        return(f'{True_Max} high flush!')
         
      if Flush == False:
        return(f'{True_Max} high')
          
  def evaluate_bet(self):
    reward = self.rank_hand()
    
           
    keys = []
    for key in self.Reward_Dict.keys():
      keys.append(key)
    key = []
    for i in range(len(keys)):
      val = keys[i]
      if val in reward:
        key.append(val)
    if len(key)>0:
      for k,v in self.Reward_Dict.items():
        if key[0]== k:
          return v 
    return 0  
      

# player = Player('Jesse')
# # print(player.Chips)
# player.five_card_draw()
# player_2 = Player('Steve')
# # print(player_2.draw(5))
# player_2.five_card_draw()
# # player_2.save_chips()
# print(player_2.Chips)
player = Player('Steve')


player.five_card_draw()


# player.draw(5)
# player.evaluate_bet()
# print(player.bet())
#TODO create function that identifies player's hand, pair, full house, straight, etc

