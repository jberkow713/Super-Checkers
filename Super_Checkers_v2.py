import turtle
import time
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
#Total is list of actual coordinates of all indices
Total_Up = A[3]
#Total_Up is list of coordinates to be highlighted for user, in middle of squares, for all indices
# print(Total)
# print(Total_Up)

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
            
            
    if Color=='red':
        new_moves = [x for x in Moves if x not in Red.keys()]
                        
        if Color=='red':
            #Check to see if spots it can move to are red, for jumping
            Possible_Jumps = [x for x in new_moves if x in Black.keys()]
            
    #Jumps represent spots of opposite color in the way, only way they can actually be jumps, is if the spot behind them
    # in the direction from the piece, is empty, meaning it is in the Possible_Spots Dictionary
    Jump_Options = []
    for piece in Possible_Jumps:
        #For most pieces this will work, but not if the jump is moving off the edge of the board
        
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
    pen.circle(20)
    pen.end_fill()
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

def choose_piece():
    #Lights up board with possible spots to move to
    position = player.pos()
    index = []
    for k,v in Total_Up.items():
        if v == position:
            index.append(k)
    Trigger = 0        
    
    for k,v in Red.items():
        if k == index[0]:
            coords = tuple([v[0], v[1]])
            possible_spots = find_piece_movement((coords))
            Trigger = 1
                
    for k,v in Black.items():
        if k == index[0]:
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
                
        time.sleep(2)
        for x in positions:
            draw_circle(x[0], x[1]-20, 'white')               

    
    
    def move_to_spot():
        last_index = index[0]
        
        for k,v in Red.items():
            if last_index == k:
                drawing_color = 'red'
        for k,v in Black.items():
            if last_index ==k:
                drawing_color = 'black'

        possible_locations = keys_to_move_to
        
        Locations = []
        for k,v in Total_Up.items():
            for x in possible_locations:
                if x == k:
                    Locations.append(v)
        
        
        if player.pos() in Locations:
            Moved_to_Square = player.pos()
            # print(last_index)
            # print(Moved_to_Square)
            for k,v in Total_Up.items():
                if k == last_index:
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
            # def draw_circle_full(x,y,color):
            #     pen = turtle.Turtle()
            #     pen.up()
            #     pen.setpos(x,y)        
            #     pen.speed(100)
            #     pen.color(color)
            #     pen.down()
            #     pen.begin_fill()
            #     pen.circle(49)
            #     pen.end_fill()
            draw_circle_full(Erased_Coordinate[0], Erased_Coordinate[1], 'white')
            draw_circle_full(Drawing_Coordinate[0], Drawing_Coordinate[1], drawing_color)
            if drawing_color == 'black':
                del Black[last_index]
                Black[Moved_to_key] = tuple([Drawing_Coordinate[0], Drawing_Coordinate[1], 'normal'])
                print(Black) 
            if drawing_color == 'red':
                del Red[last_index]
                Red[Moved_to_key] = tuple([Drawing_Coordinate[0], Drawing_Coordinate[1], 'normal'])
            # print(Erased_Coordinate)
            # print(Drawing_Coordinate)
            # print(drawing_color)
            # print(last_index)
            # print(Moved_to_key)

            #Drawing Coordinate shows where to draw new circle from                 



                    

    turtle.onkey(move_to_spot, 'Return')


    
    




          
            

turtle.listen()
turtle.onkey(move_left, "Left") 
turtle.onkey(move_right, "Right")
turtle.onkey(move_up, "Up") 
turtle.onkey(move_down, "Down")
turtle.onkey(choose_piece, 'space')
   

#TODO Once piece moves, we need to change it's key, redraw it, etc


#Once the piece moves to the new coordinate, the index of the piece in that specific color dictionary, needs to be
#changed to the new index, and if possible, the type of piece needs to be altered as well. If the type of piece changes, 
# The color of the piece needs to be changed, to say Orange for Red's pieces, and Blue for Black's pieces, indicating that piece
# is now a king

# If player chooses to jump opponent's piece, we need to also clear the opponent's piece from the board, change it's value in its
#own dictionary, add it to the "knocked out" list





turtle.done()



