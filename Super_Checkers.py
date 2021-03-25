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
    Black = list(range(0,2*squares_per_row))
    
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
Red = A[1]
Total = A[2]


def find_open_spots(Black_Dict, Red_Dict, Total_Dict):
    '''
    Takes in Black and Red Dictionary of checkers, checks them against overall dictionary,
    returns open possible positions to move to
    '''
    Positions = []
    
    for v in Total_Dict.values():
        Positions.append(v)
    for v in Black_Dict.values():
        x = tuple([v[0], v[1]])
        Positions.remove(x)
    for v in Red_Dict.values():
        x = tuple([v[0], v[1]])
        Positions.remove(x)
      

    return Positions

print(find_open_spots(A[0], A[1], A[2]))



       

 









#-boardsize/2, -boardsize/2

#Create Checkers, Red/Black

#Also need to give each checker a current position, based on the center of the checker
#It has to move to a spot that another checker is not currently occupying
#So the function needs to create the checkers, and also create a dictionary of the checkers starting positions
#When a piece moves, basically we check the future position, if it is open, we remove the checker from the current
#position by erasing it's current checker, and then draw it at the new position 

#List of open positions, just based on the center of the piece, on the board
#List of checkers and their coordinates/status(coordinates of center)...
#Possible statuses... Off, Normal, King, Super-King, God
#So each piece has a number as its Key, and their value is a list of [Coordinate, status]

#For the user, once piece has been clicked, we check it's coordinate and status to see its possible moves
#possible moves are moves it CAN go to that are unoccupied
# user then clicks on spot he wants piece to move to, if unoccupied it moves
# user can unclick piece, and choose new piece
# once piece moves, its status and coordinates are updated

#First player to knock out all other players pieces wins
# Normal pieces can move forward at a left diagonal, forward, forward at a right diagonal...one space at a time
#If a normal piece jumps another piece, it becomes a king
## Kings can move any direction, one space at a time,  if it jumps a piece, it becomes a Super King
### Super Kings can move any direction, 1-3 spaces at a time, but only in one consistent direction, once it jumps
# a piece, it becomes a God
#### Gods can move any direction,1-4 spaces at a time, and are able to change their direction each time they
# move, so they can go forward one, forward diagonal, left, then back....etc, or they can just go forward one 
#spot, etc

#TODO Create starting checkers, their coordinates, and create the dictionary that stores them, so function 
# will both map and draw the different colored checkers, and it will return a dictionary for each circle

#Then we need a movement function, finds possible positions of each piece, returns an updated dictionary
# based on movement of particular piece, and its interaction with the board and other pieces, so this function
# will move one piece, and return updated dictionary

# And that will be the game, it will continue until players quit, or ALL pieces from one color have their 
# status as "OFF", then game will close

#As statuses of pieces change, so will their colors
#King = Blue
#Super King = Green
#God = Orange











turtle.done() 