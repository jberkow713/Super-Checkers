import turtle
import time
import random 
#Create Board
import gym
import numpy as np
import math

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
    
    Positions = [value for value in Total.values()] 
    
    for v in Black.values():
        x = tuple([v[0], v[1]])
        Positions.remove(x)
    for v in Red.values():
        x = tuple([v[0], v[1]])
        Positions.remove(x)
    for k,v in Total.items():
        if v in Positions:
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

print(find_piece_type((-350.0, -300.0)))

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
    # Coordinate:(-350.0, -300.00)
   
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
      
    if Color=='black':
        
        new_moves = [x for x in Moves if x in Possible_Spots.keys()]          
        if Color=='black':
            #Check to see if spots it can move to are red, for jumping
            Possible_Jumps = [x for x in Moves if x in Red.keys()]
        
            
    if Color=='red':
        
        new_moves = [x for x in Moves if x in Possible_Spots.keys()]
                        
        if Color=='red':
            #Check to see if spots it can move to are red, for jumping
            Possible_Jumps = [x for x in Moves if x in Black.keys()]
        
         
    Final_Possible_Spots = []
    Jump_Options = []
    if Index % squares_per_row != 0 and Index % squares_per_row != (squares_per_row-1):
        if Index > (squares_per_row-1) or Index < (squares_per_row  * (squares_per_row-1)):
            for piece in Possible_Jumps:
                        
                if piece % squares_per_row != 0 and piece % squares_per_row != (squares_per_row-1) \
                    and piece < (squares_per_row  * (squares_per_row-1)) and piece> (squares_per_row-1):
                
                    Direction = piece - Index
                    Jump_to_index = piece+Direction
                    for k in Possible_Spots.keys():
                        if Jump_to_index == k:
                            Jump_Options.append(Jump_to_index)
                            Final_Possible_Spots.append(piece)
        if Index < (squares_per_row) or Index > (squares_per_row*(squares_per_row-1)):
            for piece in Possible_Jumps:
                if piece % squares_per_row !=0 and piece % squares_per_row != (squares_per_row-1):

                    Direction = piece - Index
                    Jump_to_index = piece+Direction
                    for k in Possible_Spots.keys():
                        if Jump_to_index == k:
                            Jump_Options.append(Jump_to_index)
                            Final_Possible_Spots.append(piece)

    if Index % squares_per_row == 0 or Index % squares_per_row == (squares_per_row-1):
        if Index >=(squares_per_row)*(squares_per_row-1) or Index < squares_per_row:
            for piece in Possible_Jumps:

                Direction = piece - Index
                Jump_to_index = piece+Direction
                for k in Possible_Spots.keys():
                    if Jump_to_index == k:
                        Jump_Options.append(Jump_to_index)
                        Final_Possible_Spots.append(piece)
        elif Index < (squares_per_row  * (squares_per_row-1)) and Index > (squares_per_row-1):
            for piece in Possible_Jumps:

                if piece < (squares_per_row  * (squares_per_row-1)) and piece> (squares_per_row-1):

                    Direction = piece - Index
                    Jump_to_index = piece+Direction
                    for k in Possible_Spots.keys():
                        if Jump_to_index == k:
                            Jump_Options.append(Jump_to_index)
                            Final_Possible_Spots.append(piece)
   
    Jump_Dict = dict(zip(Jump_Options, Final_Possible_Spots ))
    
    return new_moves, Jump_Dict          

# print(find_piece_movement((-350.0, -300.00)))

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

#Player_Red is a global variable, to be used to condition whether a player can move as Red or Black within the function
#For whatever reason, this is the only way to get this to work within Turtle functions
Player_Color = 'red'

INDEX = 99 
Forced_Key = 100 
Current_Piece = 101 
def choose_piece():
    '''
    Shows player where they can move to, for a given piece and given color, given the global variable
    They then move using the move_to_spot function within
    They are limited to move only the color which Player_Color is, and in the event of a jump, they must move
    the jumped piece again until they make a non jumped move
    '''
    position = player.pos()
       
    for k,v in Total_Up.items():
        if v == position:
            index=k
            
    Trigger = 0        

    if Player_Color =='red':
        if INDEX == Current_Piece:
                
            for k,v in Red.items():
                          
                    if k == index == Forced_Key:
                        coords = tuple([v[0], v[1]])
                        possible_spots = find_piece_movement((coords))
                        Trigger = 1
            
        if INDEX != Current_Piece:    
            for k,v in Red.items():
                

                    if k == index :
                        coords = tuple([v[0], v[1]])
                        possible_spots = find_piece_movement((coords))
                        Trigger = 1
      
    if Player_Color == 'black' :
        if INDEX == Current_Piece:

            for k,v in Black.items():
                   
                    if k == index == Forced_Key:
                                    
                        coords = tuple([v[0], v[1]])
                        possible_spots = find_piece_movement((coords))
                        Trigger = 1
        
        if INDEX != Current_Piece:   
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
            
            global Current_Piece
            Current_Piece = Moved_to_key
                            

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
                #Need to keep track of this Moved_to_key, because turn is not over after a jump, must move that key again
                global INDEX
                INDEX = index 

                global Forced_Key
                Forced_Key = Moved_to_key
      
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


def computer_moves(**kwargs):
    '''
    Takes in multiple arguments, if there is no forced key, only takes in keyword argument
    color=____, if position needs to be forced, takes in additional argument index =_____
    '''
    forced_key = 99

    for k,v in kwargs.items():
        if k == 'color':
            color = v
        if k == 'index':
            forced_key = v

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
    jump_keys = []

    if forced_key<99:

        for k,v in Pieces_to_check.items():
            if k == forced_key:
                a = tuple([v[0], v[1]])
                movement = find_piece_movement(a)
                if len(movement[1])>0:
                    jump_keys.append(k)
                        
                moves.append(movement)
                keys.append(k)
                random_keys.append(k)
      
    elif forced_key==99:

        for k,v in Pieces_to_check.items():
            a = tuple([v[0], v[1]])
            movement = find_piece_movement(a)
            if len(movement[0])>0 or len(movement[1])>0:
                if len(movement[1])>0:
                    jump_keys.append(k)
                    
                moves.append(movement)
                keys.append(k)
                random_keys.append(k)
    # print(moves)
    
    movement_dictionary = dict(zip(keys, moves))
    #random_keys represents all possible checkers for a given color that are able to move    

    #{48: ([40, 41], {}), 49: ([41, 40, 42], {}), 
    # 50: ([42, 41, 43], {}), 51: ([43, 42, 44], {}),
    #  52: ([44, 43, 45], {}), 53: ([45, 44, 46], {}), 
    # 54: ([46, 45, 47], {}), 55: ([47, 46], {})}
    if len(jump_keys)>0:
        length = len(jump_keys)
        random_key = random.randint(0, length-1)
        key = jump_keys[random_key]
    #Choose random key from possible moves
    elif len(jump_keys)==0:
        length = len(random_keys)
        random_key = random.randint(0,length-1)
        #random key represents all possible indexes of the random_key list
        key = random_keys[random_key]
        #key is index of piece being moved
              
    Random_Moves = movement_dictionary[key]
    #example : ([16, 17], {})
    #Random Moves is now the chosen key's movement options
    non_jumps = len(Random_Moves[0])
    jumps = len(Random_Moves[1].keys())

    if non_jumps >0 and jumps >0:
        is_jumped = 1
        # Temporarily forcing a jump if jump is possible, to improve gameplay
        # and speed things up
          
    if non_jumps>0 and jumps==0:
        is_jumped = 0
    if non_jumps == 0 and jumps >0:
        is_jumped = 1    

    

    moves = []
    if is_jumped == 0:
        
        for x in Random_Moves[0]:
            moves.append(x)
        
        length = len(moves)
        random_key = random.randint(0,length-1)
        
        Key_to_move_to = moves[random_key]

        for k,v in Total.items():
            if k == key:
                move_from_spot = v
            if k == Key_to_move_to:
                new_spot = v
              
        draw_circle_full(move_from_spot[0], move_from_spot[1], 'white')
        #Checking to see if moved piece is a king, before deciding on the color to draw
        new_status = None
        
        if Pieces_to_check[key][2] == 'normal':
            #if the piece moving was normal, and it has now hit the edge of the board, update color
            if color == 'black':
                if Key_to_move_to < 8:
                    new_status = 'King' 
            if color == 'red':
                if Key_to_move_to>=56:
                    new_status = 'King'
            
            if new_status:
                draw_circle_full(new_spot[0], new_spot[1], Kinged_Color)
                status = new_status
            
            elif new_status==None:
                draw_circle_full(new_spot[0], new_spot[1], color)
                status = 'normal'
        
        if Pieces_to_check[key][2] == 'King':
            draw_circle_full(new_spot[0], new_spot[1], Kinged_Color)
            status = 'King'
        
        if color == 'black':
                         
        #Update Dictionary
            del Black[key]
            Black[Key_to_move_to] = tuple([new_spot[0], new_spot[1], status])
            return Key_to_move_to, 'no jump'

        elif color == 'red':
            
            del Red[key]
            Red[Key_to_move_to] = tuple([new_spot[0], new_spot[1], status])
            return Key_to_move_to, 'no jump'

    moves = []
    
    if is_jumped == 1:
        #Piece is going to make a jump
        # print(Random_Moves[1].items())
        for k,v in Random_Moves[1].items():
            moves.append(k)

        length = len(moves)
        random_key = random.randint(0,length-1)
        
        Key_to_move_to = moves[random_key]

        for k,v in Random_Moves[1].items():
            if k == Key_to_move_to:
                Jumped = v 
     
        for k,v in Total.items():
            if k == key:
                move_from_spot = v
            #Moving from this indexed spot     
            if k == Jumped:
                jumped_spot = v
            #Spot that was jumped    
            if k == Key_to_move_to:
                new_spot = v
            #Spot that is moved to     
        
        draw_circle_full(move_from_spot[0], move_from_spot[1], 'white')
        #Delete indexed spot that you are moving from
        draw_circle_full(jumped_spot[0], jumped_spot[1], 'white')
        #Delete spot of opposite color that is being jumped
        draw_circle_full(new_spot[0], new_spot[1], Jumped_Color)
        #Draw checker in the new moved to spot

        #Update Dictionary for jumped Piece
        if color == 'black':
        
            del Black[key]
            del Red[Jumped]
            Black[Key_to_move_to] = tuple([new_spot[0], new_spot[1], 'King'])
            
            return Key_to_move_to, 'jumped'
        
        if color == 'red':

            del Red[key]
            del Black[Jumped]
            Red[Key_to_move_to] = tuple([new_spot[0], new_spot[1], 'King'])
           
            return Key_to_move_to, 'jumped'

def represent_board():

  board = np.zeros((8,8), dtype=int)
  Black_Keys = []
  for x in Black.keys():
      Black_Keys.append(x)
               
  Red_Keys = []
  for x in Red.keys():
      Red_Keys.append(x)

  for x in Black_Keys:
    row =  (x // 8)
    column = x % 8
    board[row][column] = 1
  for x in Red_Keys:
    row =  (x //8)
    column = x % 8
    board[row][column] = 2 

  return board  

def find_center_mass(Board):
    '''
    Finds center of mass for black pieces, and red pieces
    '''
    
    black_result = np.where(Board==1)
    red_result = np.where(Board==2)
  
    row = 0
    column = 0
    for x in black_result[0]:
        row+=x
    for x in black_result[1]:
        column+=x
    center_row = row/len(black_result[0])
    center_column = column/len(black_result[1])

    Black_Center = tuple([center_row, center_column])

    row = 0
    column = 0
    for x in red_result[0]:
        row+=x
    for x in red_result[1]:
        column+=x
    center_row = row/len(red_result[0])
    center_column = column/len(red_result[1])

    Red_Center = tuple([center_row, center_column ])
    
    return Black_Center, Red_Center

def find_center_key():
    '''
    Finding keys in the center of mass for a given color
    '''
    
    Centers = find_center_mass(Board)
    black = Centers[0]
    red = Centers[1]
    
    black_high = math.ceil(black[1])
    black_low = math.floor(black[1])
    black_high2 = math.ceil(black[0])
    black_low2 = math.floor(black[0])
    
    
    red_high = math.ceil(red[1])
    red_low = math.floor(red[1])
    red_high2 = math.ceil(red[0])
    red_low2 = math.floor(red[0])

    Black_Centers = []
    for x in Black.keys():
        remainder = x%8
        if remainder == black_high or remainder == black_low:
            if x >= black_low2*8 and x <= (black_high2+1)*8:
                Black_Centers.append(x)
    
    Red_Centers = []
    for x in Red.keys():
        remainder = x%8
        if remainder == red_high or remainder == red_low:
            if x >= red_low2*8 and x <= (red_high2+1)*8:
                Red_Centers.append(x)

    return Black_Centers, Red_Centers
def find_center_mass_updated(color):
    if color == 'red':
        Color_Dict = Red
    if color == 'black':
        Color_Dict = Black
    
    x_coord = []
    y_coord = []
    for value in Color_Dict.values():
        if value[2] == 'normal':
            x_coord.append(value[0])
            y_coord.append(value[1])
        if value[2] == 'King':
            for i in range(3):
                x_coord.append(value[0])
                y_coord.append(value[1])
    avg_x_coord = sum(x_coord) /len(x_coord)
    avg_y_coord = sum(y_coord) / len(y_coord)

    return avg_x_coord, avg_y_coord                 

#TODO functions that incorporate the angle represented by the collective checkers for given color,
#kings given preference again

#Function to find spacing, some kind of avg spacing for a group before it hits opponents pieces,
#such as possible moves it can make, versus possible moves thats bring the pieces close to opponent
#also spacing among its own pieces

#and ultimately combine these various functions prior to each move, to find a given board state
#this will help to create the table which will be used for reinforced learning









starting_color = random.randint(0,1)

if starting_color == 0:
    Player_turn = 'black'
    
if starting_color == 1:
    Player_turn = 'red'

while len(Red)>0 and len(Black)>0:

    while Player_turn == 'black':

        print(find_center_mass_updated('black'))


        Move = computer_moves(color='black')
        if Move[1] == 'no jump':
            Player_turn = 'red'
        
        if Move[1] == 'jumped':
            Jumped =True
            index = Move[0]
            
            while Jumped == True:
                Move = computer_moves(color='black', index=index)
                if Move[1] == 'jumped':
                    index = Move[0]
                if Move[1]!='jumped':
                    Jumped=False
        

        Player_turn = 'red'             

    while Player_turn == 'red':

        print(find_center_mass_updated('red'))   
        
        Move = computer_moves(color='red')
       
        if Move[1] == 'no jump':
            Player_turn = 'black'
        
        if Move[1] == 'jumped':
            Jumped = True
            index = Move[0]
            
            while Jumped == True:
                Move = computer_moves(color='red', index=index)
                if Move[1] == 'jumped':
                    index = Move[0]
                if Move[1]!='jumped':
                    Jumped=False
             
       
        Player_turn= 'black'     
        
#TODO Create the human/computer interaction...

# When computer or human makes a move that is not a jump, then switch to opposing player, 

#Simulation of computer versus computer, to check their behavior


#TODO create representation of possible board states, 
# Use color's average coordinate, put emphasis on the positioning of kings, perhaps use their 
#coordinates double, or triple the non king's position
# For now this will be a rough estimate of the board state for any given move

#We also want to incorporate spacing from opponents pieces, and spacing related to your own pieces
#into the board state


turtle.done()



