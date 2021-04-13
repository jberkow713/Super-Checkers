import turtle
import time
import random 
#Create Board
 

def draw_board(Boardsize, squares_per_row):
    '''
    Initial Function to Create Board, Based on size of board and squares per row
    Also creates 3 dictionaries: Dictionary of all the Red Squares and their positions, 
    Dictionary of all Black Squares and their positions, and a General dictionary of all 
    Squares and their positions
    '''    
       
    sc = turtle.Screen()
    sc.setup(Boardsize, Boardsize)
    pen = turtle.Turtle()
    pen.speed(100)
    pen.up()
    pen.setpos(-Boardsize/2,-Boardsize/2)
    pen.down()
    def draw_square(Boardsize, squares_per_row):
    
        for _ in range(4):
            pen.forward(Boardsize/squares_per_row)
            pen.left(90)
                
        pen.forward(Boardsize/squares_per_row)
    def draw_circle(Boardsize, squares_per_row, color):
        
        pen.speed(100)
        pen.color(color)
        pen.down()
        pen.begin_fill()
        pen.circle(((Boardsize/squares_per_row)/2)-1)
        pen.end_fill()
    
    for row in range(1,squares_per_row+1):
        
        for i in range(squares_per_row):
            draw_square(Boardsize, squares_per_row)
        pen.up()
        pen.setpos((-Boardsize/2), ((-Boardsize/2)+row*(Boardsize/squares_per_row)))
        pen.down()
    
    pen.up()
    pen.setpos((-Boardsize/2)+.5*(Boardsize/squares_per_row), (-Boardsize/2))    
    #Red's Pieces
    Red = list(range(0,2*squares_per_row))
    #Black's Pieces
    Black = list(range((squares_per_row*squares_per_row)-(2*squares_per_row),squares_per_row*squares_per_row))
    
    Black_Positions = []
    
    Red_Positions = []
    
    
    for row in range(1, 3):

        for i in range(squares_per_row):
            
            a = round(pen.xcor(),1)
            b = round(pen.ycor(),1)
            t = tuple([a,b,'normal'])
            Red_Positions.append(t)

            draw_circle(Boardsize, squares_per_row, 'red')
            pen.forward(Boardsize/squares_per_row)

        pen.up()
        pen.setpos((-Boardsize/2)+.5*(Boardsize/squares_per_row), (-Boardsize/2)+row*(Boardsize/squares_per_row)) 
    
    
    pen.up()
    pen.setpos((-Boardsize/2)+.5*(Boardsize/squares_per_row), (Boardsize/2)-(2*(Boardsize/squares_per_row)))    
    for row in range(squares_per_row-1,squares_per_row+1):
        for i in range(squares_per_row):
            a = round(pen.xcor(),1)
            b = round(pen.ycor(),1)
            t = tuple([a,b,'normal'])
            Black_Positions.append(t)

            draw_circle(Boardsize, squares_per_row, 'black')
            pen.forward(Boardsize/squares_per_row)
        
        pen.up()
        pen.setpos((-Boardsize/2)+.5*(Boardsize/squares_per_row), (-Boardsize/2)+row*(Boardsize/squares_per_row))
     
    
    Total_Squares = list(range(0,squares_per_row*squares_per_row))
    Tuple_Position_List = []
    starting_x_cord = (-Boardsize/2)+.5*(Boardsize/squares_per_row)
    starting_y_cord = (-Boardsize/2)
    a = starting_x_cord
    b = starting_y_cord
    for i in range(0, squares_per_row):
        
        b+= i*(Boardsize/squares_per_row)
                
        for _ in range(squares_per_row):
            tup = tuple([a,b])
            Tuple_Position_List.append(tup)
            a += Boardsize/squares_per_row
        
        a = starting_x_cord
        b = starting_y_cord
        
    Total_Squares_2 = list(range(0,squares_per_row*squares_per_row))
    Tuple_Position_List_2 = []
    starting_x_cord = (-Boardsize/2)+.5*(Boardsize/squares_per_row)
    starting_y_cord = (-Boardsize/2)+((Boardsize/squares_per_row)/2)
    a = starting_x_cord
    b = starting_y_cord
    for i in range(0, squares_per_row):
        
        b+= i*(Boardsize/squares_per_row)
                
        for _ in range(squares_per_row):
            tup = tuple([a,b])
            Tuple_Position_List_2.append(tup)
            a += Boardsize/squares_per_row
        
        a = starting_x_cord
        b = starting_y_cord


    Position_Dictionary_2 = dict(zip(Total_Squares_2, Tuple_Position_List_2))     
    Position_Dictionary = dict(zip(Total_Squares, Tuple_Position_List))
    Final_Black_Dict = dict(zip(Black, Black_Positions))
    Final_Red_Dict = dict(zip(Red, Red_Positions))


    return Final_Black_Dict, Final_Red_Dict, Position_Dictionary, Position_Dictionary_2

A = draw_board(800, 8)

Black = A[0]
Red = A[1]
Total = A[2]
Total_Up = A[3]


def find_open_spots():
    '''
    Takes in Black and Red Dictionary of checkers as Global Variables, 
    checks them against overall dictionary, 
    returns a dictionary of possible open spots basically not being occupied
    by Red or Black pieces: { Key numbers, (coordinate, coordinate), etc...}
    '''
    Positions = []
    Key_Numbers = []
    
    for v in Total.values():
        Positions.append(v)
    for v in Black.values():
        x = tuple([v[0], v[1]])
        Positions.remove(x)
    for v in Red.values():
        x = tuple([v[0], v[1]])
        Positions.remove(x)
    for k,v in Total.items():
        for x in Positions:
            if x == v:
                Key_Numbers.append(k)
    Open_Positions = dict(zip(Key_Numbers, Positions))              

    return Open_Positions

# print(find_open_spots())



def find_piece_type(Coordinate):
    '''
    Creates possible spots to move to for a given piece, Use Dictionary of that piece
    and the overall dictionary of open spots
    '''
    #Access Red and Black Dictionaries
    Red_Spots = []
    Red_Types = []
    Black_Spots = []
    Black_Types = []

    
    for v in Red.values():
        x = tuple([v[0], v[1]])
        Red_Spots.append(x)
        Red_Types.append(v[2])
    for v in Black.values():
        x = tuple([v[0], v[1]])
        Black_Spots.append(x)
        Black_Types.append(v[2])
    for k,v in Total.items():
            if Coordinate == v:
                Position = k
    Red_Dict = dict(zip(Red_Spots, Red_Types))
    Black_Dict = dict(zip(Black_Spots, Black_Types))

    if Coordinate in Red_Spots:
        for k,v in Red_Dict.items():
            if Coordinate == k:
                return ('red',v,Position)
    if Coordinate in Black_Spots:
        for k,v in Black_Dict.items():
            if Coordinate == k:
                return ('black',v,Position)    

# print(find_piece_type((-350.0, -300.0)))

def find_piece_movement(Coordinate):
    '''
    Movement function, takes in Coordinate of piece, and squares per row,
    returns list of possible coordinates of possible moves, will make separate function for jumping
    This function only uses basic movement, it does not incorporate jumping
    '''
    squares_per_row=8
    Piece_Description = find_piece_type(Coordinate)
    Color = Piece_Description[0]
    Type = Piece_Description[1]
    Index = Piece_Description[2]
    # example of Piece_Description = ('red', 'normal', 0)
    Possible_Spots = find_open_spots()
    #Dictionary of open spots on the board, keys and their corresponding coordinates 
    Moves = []
    if Type== 'normal':
        if Color=='red':
            if Index< (squares_per_row*(squares_per_row-1)):
                

                if Index%squares_per_row > 0  and Index % squares_per_row < squares_per_row-1:
                    #if piece is not on an edge, and is red, and is normal
                    Moves.append(Index+squares_per_row)
                    Moves.append(Index+squares_per_row - 1)
                    Moves.append(Index + squares_per_row+1)
                elif Index % squares_per_row == 0:
                    #piece is on far left edge of board
                    Moves.append(Index+squares_per_row)
                    Moves.append(Index+squares_per_row+1)
                elif Piece_Description[2]% squares_per_row == (squares_per_row-1):
                    #piece is on far right edge of board
                    Moves.append(Index+squares_per_row)
                    Moves.append(Index+squares_per_row-1)  
        if Color=='black':
            if Index>(squares_per_row-1):
                
                if Index%squares_per_row > 0  and Index % squares_per_row < squares_per_row-1:
                    #if piece is not on an edge, and is red, and is normal
                    Moves.append(Index-squares_per_row)
                    Moves.append(Index-squares_per_row - 1)
                    Moves.append(Index - squares_per_row+1)
                elif Index% squares_per_row == 0:
                    #piece is on far left edge of board
                    Moves.append(Index-squares_per_row)
                    Moves.append(Index-squares_per_row+1)
                elif Index % squares_per_row == (squares_per_row-1):
                    #piece is on far right edge of board
                    Moves.append(Index-squares_per_row)
                    Moves.append(Index-squares_per_row-1)  
    if Type == 'King':
        if Index%squares_per_row > 0  and Index % squares_per_row < squares_per_row-1:
            if Index>(squares_per_row-1) and Index< (squares_per_row*(squares_per_row-1)):

               #King in middle area of board
                Moves.append(Index-squares_per_row-1)
                Moves.append(Index-squares_per_row)
                Moves.append(Index-squares_per_row+1)
                Moves.append(Index-1)
                Moves.append(Index+1)
                Moves.append(Index+squares_per_row-1)
                Moves.append(Index+squares_per_row)
                Moves.append(Index+squares_per_row+1)
                          

            elif Index < squares_per_row:

                # Piece is not on an edge, but is at bottom row of board
                Moves.append(Index-1)
                Moves.append(Index+1)
                Moves.append(Index+squares_per_row-1)
                Moves.append(Index+squares_per_row)
                Moves.append(Index+squares_per_row+1)
            elif Index >= squares_per_row*(squares_per_row-1):
                Moves.append(Index-squares_per_row-1)
                Moves.append(Index-squares_per_row)
                Moves.append(Index-squares_per_row+1)
                Moves.append(Index-1)
                Moves.append(Index+1)
        if Index% squares_per_row == 0:
            #King on the left side of board
            if Index>(squares_per_row-1) and Index< (squares_per_row*(squares_per_row-1)):
                
                Moves.append(Index-squares_per_row)
                Moves.append(Index-squares_per_row+1)
                Moves.append(Index+1)
                Moves.append(Index+squares_per_row)
                Moves.append(Index+squares_per_row+1)
            elif Index < squares_per_row:
                Moves.append(Index+1)
                Moves.append(Index+squares_per_row)
                Moves.append(Index+squares_per_row+1)
            elif Index >= squares_per_row*(squares_per_row-1):
                Moves.append(Index+1)
                Moves.append(Index-squares_per_row)
                Moves.append(Index-squares_per_row+1)
        if Index % squares_per_row == squares_per_row-1:
            #King on the Right side of the board
            if Index>(squares_per_row-1) and Index< (squares_per_row*(squares_per_row-1)):
                Moves.append(Index-squares_per_row-1)
                Moves.append(Index-squares_per_row)
                Moves.append(Index-1)
                Moves.append(Index+squares_per_row-1)
                Moves.append(Index+squares_per_row)
            elif Index < squares_per_row:
                Moves.append(Index-1)
                Moves.append(Index+squares_per_row-1)
                Moves.append(Index+squares_per_row)
            elif Index >= squares_per_row*(squares_per_row-1):
                Moves.append(Index-1)
                Moves.append(Index-squares_per_row)
                Moves.append(Index-squares_per_row-1)



    
    Possible_Jumps = []
       
    if Color=='black':
        new_moves = [x for x in Moves if x not in Black.keys()]
                  
        if Color=='black':
            #Check to see if spots it can move to are red, for jumping
            Possible_Jumps = [x for x in new_moves if x in Red.keys()]
            #Resetting new moves to remove spots on red pieces
            new_moves = [x for x in new_moves if x not in Possible_Jumps]
            
    if Color=='red':
        new_moves = [x for x in Moves if x not in Red.keys()]
                        
        if Color=='red':
            #Check to see if spots it can move to are red, for jumping
            Possible_Jumps = [x for x in new_moves if x in Black.keys()]
            #Resetting new moves to remove spots on black pieces
            new_moves = [x for x in new_moves if x not in Possible_Jumps]
            
    
    Jump_Options = []
    for piece in Possible_Jumps:
        
        
        if piece % squares_per_row != 0 and piece % squares_per_row != (squares_per_row-1) \
            and piece < (squares_per_row  * (squares_per_row-1)) and piece> (squares_per_row-1):
        
            Direction = piece - Index
            Jump_to_index = piece+Direction
            for k in Possible_Spots.keys():
                if Jump_to_index == k:
                    Jump_Options.append(Jump_to_index)

    Jump_Dict = dict(zip(Jump_Options, Possible_Jumps ))

    return new_moves, Jump_Dict          

print(find_piece_movement((-350.0, -300.00)))

#Movement for Player
#speed is used for how far player moves with keystroke
speed = 100

player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
Starting_pos_x = -50
Starting_pos_y = 50
player.setposition(Starting_pos_x , Starting_pos_y )
player.setheading(90)

def move_left():

                    
    x = player.xcor()
    x -= speed      
    
    if x < -350:
        x = -350
    
    player.setx(x)
    player.setpos(x, player.ycor())
    
                
def move_right():
    x = player.xcor()
    x += speed
    if x > 350:
        x = 350
    player.setx(x)
    player.setpos(x, player.ycor())
    

def move_up():
    y = player.ycor()
    y += speed
    if y >  350:
        y = 350
    player.sety(y)
    player.setpos(player.xcor(), y)
    
def move_down():
    y = player.ycor()
    y -= speed
    if y < -350:
        y = -350
    player.sety(y)
    player.setpos(player.xcor(), y)


def draw_circle(x,y,color):
    pen = turtle.Turtle()
    pen.up()
    pen.setpos(x,y)        
    pen.speed(100)
    pen.color(color)
    pen.down()
    pen.begin_fill()
    pen.circle(12)
    pen.end_fill()
    pen.up()
def draw_circle_full(x,y,color):
    pen = turtle.Turtle()
    pen.up()
    pen.setpos(x,y)        
    pen.speed(100)
    pen.color(color)
    pen.down()
    pen.begin_fill()
    pen.circle(49)
    pen.end_fill()



Player_Color = 'black' 
#Player_Red is a global variable, to be used to condition whether a player can move as Red or Black within the function
#For whatever reason, this is the only way to get this to work within Turtle functions



def choose_piece():
    '''
    Shows player where they can move to, for a given piece and given color, given the global variable
    '''
    position = player.pos()
       

    for k,v in Total_Up.items():
        if v == position:
            index=k
            
    Trigger = 0        

    if Player_Color =='red':


        for k,v in Red.items():
            if k == index:
                coords = tuple([v[0], v[1]])
                possible_spots = find_piece_movement((coords))
                Trigger = 1
      
    if Player_Color == 'black' :


        for k,v in Black.items():
            if k == index:
                coords = tuple([v[0], v[1]])
                possible_spots = find_piece_movement((coords))
                Trigger = 1 
            
    positions = []
    keys_to_move_to = []
    if Trigger ==1:

        for k,v in Total_Up.items():
            if k in possible_spots[0] or k in possible_spots[1].keys():
                keys_to_move_to.append(k)
                positions.append(v)
                #draw some kind of small blue circle at the possible values
                
                draw_circle(v[0], v[1]-20, 'blue')
                
        time.sleep(1)
        for x in positions:
            draw_circle(x[0], x[1]-20, 'white')               

    
    
    def move_to_spot():
        '''
        Will allow player to move, if spot moving to is one of the previous spots designated through 
        Choose_Piece function, will update dictionary as well
        '''

              
                
               
        for k,v in Red.items():
            if k == index:
                if v[2]=='normal':
                    drawing_color = 'red'
                elif v[2] == 'King':
                    drawing_color = 'orange'    
        for k,v in Black.items():
            if k == index:
                if v[2]=='normal':
                    drawing_color = 'black'
                elif v[2] == 'King':
                    drawing_color = 'green'   
        
        Non_Jump_Locations = []
        Jump_Locations = []
        for k,v in Total_Up.items():
            for x in keys_to_move_to:
                if x == k and x in possible_spots[0]:
                    Non_Jump_Locations.append(v)
                elif x == k and x in possible_spots[1].keys():
                    Jump_Locations.append(v)    
        
        
        if player.pos() in Non_Jump_Locations:
            #if the spot the player moves to is in the possible spots within non-jump locations
            Moved_to_Square = player.pos()
            
            for k,v in Total_Up.items():
                if k == index:
                    To_be_erased = k
            for k,v in Total.items():
                if k == To_be_erased:
                    Erased_Coordinate = v    
            
            for k,v in Total_Up.items():
                if v == Moved_to_Square:
                    Moved_to_key = k
            for k,v in Total.items():
                if k == Moved_to_key:
                    Drawing_Coordinate = v
            
            draw_circle_full(Erased_Coordinate[0], Erased_Coordinate[1], 'white')
            draw_circle_full(Drawing_Coordinate[0], Drawing_Coordinate[1], drawing_color)
            
            #Now updating dictionaries based on movement
            if drawing_color == 'black':
                del Black[index]
                Black[Moved_to_key] = tuple([Drawing_Coordinate[0], Drawing_Coordinate[1], 'normal'])
            if drawing_color == 'green':
                del Black[index]
                Black[Moved_to_key] = tuple([Drawing_Coordinate[0], Drawing_Coordinate[1], 'King'])     
            if drawing_color == 'red':
                del Red[index]
                Red[Moved_to_key] = tuple([Drawing_Coordinate[0], Drawing_Coordinate[1], 'normal'])
            if drawing_color == 'orange':
                del Red[index]
                Red[Moved_to_key] = tuple([Drawing_Coordinate[0], Drawing_Coordinate[1], 'King'])    
            

        if player.pos() in Jump_Locations:
            #if player is moving to a jumping location
            Moved_to_Square = player.pos()

            for k,v in Total_Up.items():
                if k == index:
                    To_be_erased = k
            for k,v in Total.items():
                if k == To_be_erased:
                    Erased_Coordinate = v    
            
            for k,v in Total_Up.items():
                if v == Moved_to_Square:
                    Moved_to_key = k
            for k,v in Total.items():
                if k == Moved_to_key:
                    Drawing_Coordinate = v
               
            if drawing_color == 'black' or drawing_color == 'green':
                for k,v in possible_spots[1].items():
                    if Moved_to_key == k:
                        to_be_deleted = v
                for k,v in Total.items():
                    if k == to_be_deleted:
                        Erased_Jump_Coords = v
                #This erases the moving checker's previous spot
                draw_circle_full(Erased_Coordinate[0], Erased_Coordinate[1], 'white')
                #This erases the checker that has been jumped
                draw_circle_full(Erased_Jump_Coords[0], Erased_Jump_Coords[1], 'white')
               
                del Red[to_be_deleted]
                del Black[index]
                Black[Moved_to_key] = tuple([Drawing_Coordinate[0], Drawing_Coordinate[1], 'King'])
           
            if drawing_color == 'red' or drawing_color == 'orange':
                for k,v in possible_spots[1].items():
                    if Moved_to_key == k:
                        to_be_deleted = v
                for k,v in Total.items():
                    if k == to_be_deleted:
                        Erased_Jump_Coords = v
                #This erases the moving checker's previous spot
                draw_circle_full(Erased_Coordinate[0], Erased_Coordinate[1], 'white')
                #This erases the checker that has been jumped
                draw_circle_full(Erased_Jump_Coords[0], Erased_Jump_Coords[1], 'white')

                del Black[to_be_deleted]
                del Red[index]
                Red[Moved_to_key] = tuple([Drawing_Coordinate[0], Drawing_Coordinate[1], 'King'])
                                
            
            if drawing_color == 'red':
                jumped_color = 'orange'
            elif drawing_color == 'black':
                jumped_color = 'green'    
            draw_circle_full(Drawing_Coordinate[0], Drawing_Coordinate[1], jumped_color)
            #Need to force them once they have jumped, to move same piece
    turtle.onkey(move_to_spot, 'Return')

turtle.listen()
turtle.onkey(move_left, "Left") 
turtle.onkey(move_right, "Right")
turtle.onkey(move_up, "Up") 
turtle.onkey(move_down, "Down")
turtle.onkey(choose_piece, 'space')
   

#TODO Create the computer moves, create the human/computer interaction...
#Need to write the function for the computer, it's obviously not going to use human methods for movement
# When computer or human makes a move that is not a jump, then switch to opposing player, 
# When computer or human makes a move that is a jump, force computer or human to move again with the same piece

#Want to allow computer to see all possible choices for all pieces that can move
#Going to take in a red or black color
def computer_moves(color):
    if color == 'red':
        Pieces_to_check = Red
        Jumped_Color = 'orange'
        Kinged_Color = 'orange' 
    if color == 'black':
        Pieces_to_check = Black
        Jumped_Color = 'green'
        Kinged_Color = 'green' 
    keys = []
    random_keys = []
    moves = []
    for k,v in Pieces_to_check.items():
        a = tuple([v[0], v[1]])
        movement = find_piece_movement(a)
        if len(movement[0])>0 or len(movement[1])>0:
                   
            moves.append(movement)
            keys.append(k)
            random_keys.append(k)
    print(moves)
    
    movement_dictionary = dict(zip(keys, moves))
    #in jump moves, we have dictionary of key value pairs
    #([18, 20], {11: 19})
    #first value represents ending location, value represents piece to be jumped
    #11 represents where piece can end up, 19 represents piece to be jumped 

    #Choose random key from possible moves
    length = len(random_keys)
    random_key = random.randint(0,length-1)
    key = random_keys[random_key]
    print(key)
    
    #This checks to see if the current piece being moved is a King or not, 
    #This is needed in case a piece that is already a king, is making a normal move, and
    #Then it must be drawn retaining it's new color
    if Pieces_to_check[key][2] == 'King':
        King_Color = True
    if Pieces_to_check[key][2] == 'normal':
        King_Color = False

            

        
    Random_Moves = movement_dictionary[key]
    #([45, 44, 46], {})
    moves = []
    for x in Random_Moves[0]:
        moves.append(x)
    for k,v in Random_Moves[1]:
        moves.append(k)
    #Choose index to move to 
    length = len(moves)
    random_key = random.randint(0,length-1)
    
    Key_to_move_to = moves[random_key]
    print(Key_to_move_to)
    
    
    Jump = 0
    #key is spot moved from
    #Key_to_move_to is spot moved to
    #Need to find out if the piece jumped or not
    for k,v in Random_Moves[1].items():
        if Key_to_move_to == k:
            Jump = 1
            Jumped = v 

    if Jump == 1:
        for k,v in Total.items():
            if k == key:
                move_from_spot = v 
            if k == Jumped:
                jumped_spot = v
            if k == Key_to_move_to:
                new_spot = v 
        draw_circle_full(move_from_spot[0], move_from_spot[1], 'white')
        draw_circle_full(jumped_spot[0], jumped_spot[1], 'white')
        draw_circle_full(new_spot[0], new_spot[1], Jumped_Color)
        #Update Dictionary for jumped Piece
        if color == 'black':

        
            del Black[key]
            del Red[Jumped]
            Black[Key_to_move_to] = tuple([new_spot[0], new_spot[1], 'King'])
            print(Black)
        
        if color == 'red':

            del Red[key]
            del Black[Jumped]
            Red[Key_to_move_to] = tuple([new_spot[0], new_spot[1], 'King'])
            print(Red)

        

    if Jump == 0:
        for k,v in Total.items():
            if k == key:
                move_from_spot = v
            if k == Key_to_move_to:
                new_spot = v     
        draw_circle_full(move_from_spot[0], move_from_spot[1], 'white')
        #Checking to see if moved piece is a king, before deciding on the color to draw
        if King_Color == False:
            draw_circle_full(new_spot[0], new_spot[1], color)
        elif King_Color == True:
            draw_circle_full(new_spot[0], new_spot[1], Kinged_Color)


        if color == 'black':

        #Update Dictionary
            del Black[key]
            Black[Key_to_move_to] = tuple([new_spot[0], new_spot[1], 'normal'])
            print(Black)
        elif color == 'red':

            del Red[key]
            Red[Key_to_move_to] = tuple([new_spot[0], new_spot[1], 'normal'])
            print(Red)
    

    

computer_moves('black')



turtle.done()



