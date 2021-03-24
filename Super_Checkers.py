import turtle
#Create Board
 

def draw_board(Boardsize, squares_per_row):
    '''
    Initial Function to Create Board, Based on size of board and squares per row
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
    
    for row in range(1,squares_per_row+1):
        
        for _ in range(squares_per_row):
            draw_square(Boardsize, squares_per_row)
        pen.up()
        pen.setpos((-Boardsize/2), ((-Boardsize/2)+row*(Boardsize/squares_per_row)))
        pen.down()
       
 

draw_board(800, 8)

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

#TODO Create starting checkers, their coordinates, and create the dictionary that stores them











turtle.done() 