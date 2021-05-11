def create_purpose():

    favorite_events = []
    print('Time to figure out your 5 favorite events')
    for i in range(5):
        
        favorite = input('Please type your favorite life events:')
        favorite_events.append(favorite)


    rankings = []
    for x in favorite_events:
        print(f'Please rank {x} from 1 to 10 in the following prompt:')
        variable = False
        while variable == False:
            is_decimal = False
            while is_decimal == False:
                ranking = input(f'Please rank {x} from 1 to 10:')
                if ranking.isdecimal() == True:
                    is_decimal = True
            ranking = int(ranking)
            variable = True 
        rankings.append(ranking)

    event_dict = dict(zip(favorite_events, rankings))        
    return event_dict




print(create_purpose())