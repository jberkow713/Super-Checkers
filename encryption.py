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
        
        
        final = new_val%256
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
    
    primes_again = [11,13,17,19,23,29,31,37,41,43]
    length = len(new_vals)
    index1 = 0
    
    enumed = list(enumerate(new_vals))
    indices = []
    primes = [7,11,13,17,19,23]
    
    for x in enumed:
        if x[1] == 0:
            current = x[0]
            remainder_list = []
            for y in primes:
                
                z = current%y
                remainder_list.append(z)
                remainder_dict = dict(zip(primes, remainder_list))
                
                minimum = min(remainder_dict, key=remainder_dict.get)
                
                new_vals[x[0]]=minimum*current
    final_primes = [11,13,17,21,23,29,31,37]
    final_vals = []
    for x in new_vals:
        remainder_list = []
        for y in final_primes:
            z = x%y
            remainder_list.append(z)
            remainder_dict = dict(zip(final_primes, remainder_list))
            
        maximum = max(remainder_dict, key= remainder_dict.get)
        final_vals.append(maximum)
    length = 100
    index = 0
    final_list = []
    while length >0:
        new_val = new_vals[index]* final_vals[index]
        new_val = new_val %256
        final_list.append(new_val)
        index +=1
        length -=1
       
           
    lst = []
    for x in final_list:
        y = chr(x)
        lst.append(y)
        encrypted = ''.join(lst)

    return encrypted

print(encode_basic('hiawepoakwpe okwaop ekapowk epoawk epokwerpoijwq epoqjw [epoqwj e[qjpow e[qwjpoe [qwoje[qwjpoe [qwpoje [qowje[q wej'))
# print(encode_basic('hello'))
