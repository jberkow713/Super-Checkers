import random
from collections import Counter
import json


class Card():
  def __init__(self,suit,value):
    self.suit = suit
    self.value = value

  def show(self):
    print(f"{self.value} of {self.suit}" )
  def __repr__(self):
    return f'{self.value} of {self.suit}'  
        

class Deck():
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

class Player():
  
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
    
    NAME = self.name

    for k,v in chips.items():
      if NAME== k:
        print(f"Welcome back {self.name}")

        return v 
             
    else:
      print('Welcome New Player')
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
    ace_high = ['Ace', '2', '3', '4','5']    
    if max_count == 1:
      #checking for non pairs
      for key in num_counts.keys():
        cards.append(key)
      
    
    
    length = len(ace_high)
    index = 0
    count = 0
    while length >0:
      val = ace_high[index]
      for x in cards:
        if val == x:
          count +=1
      length -=1
      index+=1

    if count ==5:
      
      if Flush == True:
        return('straight flush')
      else:
        return('5 high straight')  
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
            return('straight flush')
            
        if Flush == False:
          return(f'{True_Max} high straight')  
               
      #Applying Flush or Non Flush 
      if Flush == True:
        return(f'{True_Max} high flush!')
         
      if Flush == False:
        return(f'{True_Max} high')
  
  def texas_holdem(self):

    house = []
    for i in range(3):
      house.append(self.deck.draw())
    self.draw(2)
    #TODO insert betting
    print(house)
    for i in range(1):
      house.append(self.deck.draw())
    print(house)
    for i in range(1):
      house.append(self.deck.draw())
    print(house)
    
    self.discard()
    num_cards = len(self.hand)
    
    while num_cards>0:
      
      string_hand = []
      for x in house:
        y = str(x)
        string_hand.append(y)
    
      lst = enumerate(string_hand)
      
      print(f'The board is  {house}')
      print(f'You must discard {num_cards} from the board, you have {num_cards} left to discard')
      card = input("Which card would you like to discard?")
      for x in lst:
        if card == x[1]:
          del house[x[0]]
                    
          num_cards-=1     

    self.hand = self.hand + house
    print(self.rank_hand())
    return self.rank_hand()

  def evaluate_bet(self):
    reward = self.rank_hand()
    print(reward)
    
           
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

class Table():
  # Loads in players based on who is in list
  # overrides their deck with a collective deck
  #TODO create collaborative games using 5 card hands

  def __init__(self, players, table_number):
    
    self.players = players
    self.table_number = table_number
    self.deck = self.create_deck()
    self.Players = self.create_players()

  def create_deck(self):
    table_deck = Deck()
    table_deck.shuffle()
    deck = table_deck
    
    return deck

    
  def create_players(self):
    
    players = []
    for x in self.players:
      y = Player(x)
      y.deck = self.deck

                   
      print()
      print(f'Welcome to table {self.table_number}, {y.name}, Good luck!')
      
      print('--------------------------------------------------------------')

      players.append(y)
    return players  
  def five_card_draw(self):
    names = []
    hands = []
    scores = []
    bonus_pot = 0
    for x in self.Players:
      
      print(f"It is now {x.name}'s turn")
      bet_total = 1000 
      x.draw(5)
      x.showhand()
      wager = x.bet()
      bet_total += wager
      bonus_pot += bet_total
      x.discard()
      hand = len(x.hand)
      x.draw(5-hand)
      multiplier = x.evaluate_bet()
      
      names.append(x.name)
      scores.append(multiplier)
    
      if multiplier == 0:
        print(f'You lose {bet_total} chips. You have {x.Chips} chips remaining.')
        x.save_chips()
        
      final_return = multiplier * bet_total
      x.Chips += final_return
      print(f'Your hand was {x.rank_hand()}, you currently have {x.Chips} Chips remaining!')

      x.save_chips()
       
    
    
    score_dict = dict(zip(names, scores))
    
    print(score_dict)



    max_scores = []
    for v in score_dict.values():
      max_scores.append(v)
    high_score = max(max_scores)
    
    


    if high_score >0:
      winning_players = []
          
      for k,v in score_dict.items():
        if v == high_score:
          winning_players.append(k)
      length_winners = len(winning_players)
      added_pot = bonus_pot/length_winners

      
      for x in self.Players:
        name = x.name
        if name in winning_players:
          x.Chips += added_pot

          print(f'Congratulations {x.name}. You had the best hand at the table, you are rewarded an additional {added_pot}!')

          x.save_chips()








    

    
    



table_1 = Table(['Billyy', 'Johnyy', 'Steve', 'Jesse', 'Amy'], 1)
table_1.five_card_draw()


  

















# # print(player_2.Chips)
# player = Player('Amy')



# player.five_card_draw()


# player.draw(5)
# player.evaluate_bet()
# print(player.bet())
#TODO create function that identifies player's hand, pair, full house, straight, etc

