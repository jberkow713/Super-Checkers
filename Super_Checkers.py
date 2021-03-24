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
    pen.setpos(-400,-400)
    pen.down()
    def draw_square(Boardsize, squares_per_row):
    
        for i in range(4):
            pen.forward(Boardsize/squares_per_row)
            pen.left(90)
        pen.forward(Boardsize/squares_per_row)
    
    for row in range(1,squares_per_row+1):
        
        for i in range(squares_per_row):
            draw_square(Boardsize, squares_per_row)
        pen.up()
        pen.setpos((-Boardsize/2), ((-Boardsize/2)+row*(Boardsize/squares_per_row)))
        pen.down()    
 

draw_board(800, 10)



turtle.done() 