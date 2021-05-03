import math 

def encode_basic(word):
    word = word.replace(' ', '')
    x = bytearray(str.encode(word))
    byte_list = []
    for letter in x:
        byte_list.append(letter)
    
    val_list = [7,11,13,17,19,23]
    new_vals = []
    for x in byte_list:
        remainder_list = []
        for y in val_list:
            z = x%y
            remainder_list.append(z)
        remainder_dict = dict(zip(val_list, remainder_list))
        minimum = min(remainder_dict, key=remainder_dict.get)
        maximum = max(remainder_dict, key=remainder_dict.get)
        new_val = minimum * maximum * x 
        
        
        final = new_val%1024
        new_vals.append(final)
    if len(new_vals)<100:
        length = len(new_vals)
        new_vals.extend([0] * (100 - length))

    if len(new_vals)>100:
        length = len(new_vals)
        gaps = math.ceil(length/100)
        new_vals.extend([0]*((100*gaps)- length))
        
        length = len(new_vals)
        new_vals2 = []
        index =0 
        while length >0:
            small_sum = sum(new_vals[index:index+gaps])
            new_vals2.append(small_sum)

            length-=gaps
            index += gaps

        new_vals = []
        for x in new_vals2:
            new_vals.append(x)
    #TODO
    #Got sequences into len 100, now we have to do things to these sequences, so that similar letters
    #do not appear the same
           
    lst = []
    for x in new_vals:
        x = x % 255
  
        y = chr(x)
        lst.append(y)
        aa = ''.join(lst)

    return aa, new_vals

print(encode_basic('helloo my name is peter I am a zebra and a yakawekwapoekpoawkepoawk eawokpeeeeeeeeeeeeeeeeeeeeeeeeeeeeeapwokepoawkepkoawpkoepaowkekaowpkepawokepaowkepaowkepokawpekawokepoakwpeokawpeokawpoekpawkoepoawkepoakwepokawpeokwapekwaopek'))
print(encode_basic('hello'))
