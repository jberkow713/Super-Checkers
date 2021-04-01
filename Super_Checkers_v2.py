import turtle
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
        



       
    Position_Dictionary = dict(zip(Total_Squares, Tuple_Position_List))
    Final_Black_Dict = dict(zip(Black, Black_Positions))
    Final_Red_Dict = dict(zip(Red, Red_Positions))


    return Final_Black_Dict, Final_Red_Dict, Position_Dictionary

A = draw_board(800, 8)

Black = A[0]
# print(Black)
Red = A[1]
Total = A[2]
# print(Red)


def find_open_spots():
    '''
    Takes in Black and Red Dictionary of checkers as Global Variables, 
    checks them against overall dictionary, 
    returns a dictionary of possible open spots: { Key numbers, (coordinate, coordinate), etc...}
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

print(find_open_spots())



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

def find_piece_movement(Coordinate, squares_per_row):
    '''
    Movement function, takes in Coordinate of piece, and squares per row,
    returns list of possible coordinates of possible moves, will make separate function for jumping
    This function only uses basic movement, it does not incorporate jumping
    '''
    Piece_Description = find_piece_type(Coordinate)
    # example of Piece_Description = ('red', 'normal', 0)
    Possible_Spots = find_open_spots()
    #Dictionary of open spots on the board, keys and their corresponding coordinates 
    Possible_movement_Keys = []
    if Piece_Description[1]== 'normal':
        if Piece_Description[0]=='red':
            if Piece_Description[2]< (squares_per_row*(squares_per_row-1)):
                Possible_movement_Keys.append('red')

                if Piece_Description[2]%squares_per_row > 0  and Piece_Description[2] % squares_per_row < squares_per_row-1:
                    #if piece is not on an edge, and is red, and is normal
                    Possible_movement_Keys.append(Piece_Description[2]+squares_per_row)
                    Possible_movement_Keys.append(Piece_Description[2]+squares_per_row - 1)
                    Possible_movement_Keys.append(Piece_Description[2] + squares_per_row+1)
                elif Piece_Description[2]% squares_per_row == 0:
                    #piece is on far left edge of board
                    Possible_movement_Keys.append(Piece_Description[2]+squares_per_row)
                    Possible_movement_Keys.append(Piece_Description[2]+squares_per_row+1)
                elif Piece_Description[2]% squares_per_row == (squares_per_row-1):
                    #piece is on far right edge of board
                    Possible_movement_Keys.append(Piece_Description[2]+squares_per_row)
                    Possible_movement_Keys.append(Piece_Description[2]+squares_per_row-1)  
        if Piece_Description[0]=='black':
            if Piece_Description[2]>(squares_per_row-1):
                Possible_movement_Keys.append('black')
                if Piece_Description[2]%squares_per_row > 0  and Piece_Description[2] % squares_per_row < squares_per_row-1:
                    #if piece is not on an edge, and is red, and is normal
                    Possible_movement_Keys.append(Piece_Description[2]-squares_per_row)
                    Possible_movement_Keys.append(Piece_Description[2]-squares_per_row - 1)
                    Possible_movement_Keys.append(Piece_Description[2] - squares_per_row+1)
                elif Piece_Description[2]% squares_per_row == 0:
                    #piece is on far left edge of board
                    Possible_movement_Keys.append(Piece_Description[2]-squares_per_row)
                    Possible_movement_Keys.append(Piece_Description[2]-squares_per_row+1)
                elif Piece_Description[2]% squares_per_row == (squares_per_row-1):
                    #piece is on far right edge of board
                    Possible_movement_Keys.append(Piece_Description[2]-squares_per_row)
                    Possible_movement_Keys.append(Piece_Description[2]-squares_per_row-1)  
    
    Possible_Coordinates = []
    Possible_Jumps = []
    #This is going to take care of all movement that doesn't run into piece of opposite color
    print(Possible_movement_Keys)
    if Possible_movement_Keys[0]=='black':
        #Check to see if spots it can move to are red, for jumping
        for x in Possible_movement_Keys:
            for k,v in Red.items():
                if x == k:
                    Possible_Jumps.append(v)
            for k,v in Possible_Spots.items():
                #if spots are empty
                if x == k:
                    Possible_Coordinates.append(v)
    if Possible_movement_Keys[0]=='red':
        #Check to see if spots it can move to are black, for jumping
        for x in Possible_movement_Keys:
            for k,v in Black.items():
                if x == k:
                    Possible_Jumps.append(v)
            for k,v in Possible_Spots.items():
                #if spots are empty
                if x == k:
                    Possible_Coordinates.append(v)
    
    return Possible_Coordinates, Possible_Jumps            

print(find_piece_movement((-350.0, -300.00), 8))
turtle.done()



