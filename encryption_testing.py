import random

def or_addition(letter):
  a_bytes = list(bytes(letter, "ascii"))
  a = (bin(a_bytes[0])[2:])
  
  a = a.zfill(9)
  
    
  b = random.randint(0,256)
  b = bin(b)[2:]
  b = b.zfill(9)

  #need to add 2 in or operation

  length = 9
  index =0
  binary_list = []
  while length >0:
    A = a[index]
    B = b[index]
    if A == B:
      binary_list.append(str(0))
    else:
      binary_list.append(str(1))

    length -=1
    index +=1

  outcome = ''.join(binary_list)
     

  return outcome


 
def scramble_word(string):

  string = string.replace(" ", "")
  letters = [x for x in string]
  length = len(string)
  random_list = []

  while length>0:
    changed_length =len(letters)
    enum = list(enumerate(letters))
    
    rand_index = random.randint(0,changed_length-1)
    
    for x in enum:
      if rand_index == x[0]:
        random_list.append(x[1])
        letters.remove(x[1])
    
    length-=1

  scrambled_word = ''.join(random_list)
  
  return scrambled_word


def encrypt_v2(string):
  #returns scrambled and encrypted string each time different for given value

  scrambled = scramble_word(string)
  scrambled_list = []
  scrambled_list = [or_addition(x) for x in scrambled]
   
  joined_list = ''.join(scrambled_list)  
  return joined_list



print(encrypt_v2('hello world'))