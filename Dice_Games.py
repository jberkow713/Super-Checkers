import random
from collections import Counter 
class Die():
    pass 
                
    def roll(self):
        roll = random.randint(0,6)
        self.value = roll
        return self.value

    def __repr__(self):
        return f'You rolled {self.value} '  


J = Die()
J.roll()
print(J.value)



def roll_dice(num_dice):
    dice = []
    for _ in range(num_dice):
        die = random.randint(0,6)
        dice.append(die)
    return dice   
def gamble(rolls, bet):
    rolls = roll_dice(rolls)
    variable = False
    while variable == False:
      is_decimal = False
      while is_decimal == False:
          prediction = input("What is the most common roll?")
          if prediction.isdecimal() == True:
              is_decimal = True
      prediction = int(prediction)
      variable = True
    
    Rolls = Counter(rolls)
    maximum = max(Rolls, key=Rolls.get)
    if prediction == maximum:
        print(f'The most common roll was {prediction}, You win {bet}')
        print(rolls)
        return bet
    else:
        print(f'You predicted {prediction} as the most common roll, it actually was {maximum}, you lose your bet')
        print(rolls)
        return 0     

gamble(50, 100)
