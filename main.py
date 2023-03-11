from turtle import Turtle, Screen
import random
import time

screen = Screen()

# Cage field
field = Turtle()
field.hideturtle()
field.speed("fastest")
field.penup()
field.left(90)
field.fd(75)
field.left(90)
field.fd(25)
field.pendown()
field.left(90)
field.fd(150)
field.penup()
field.left(90)
field.fd(50)
field.pendown()
field.left(90)
field.fd(150)
field.penup()
field.bk(50)
field.pendown()
field.left(90)
field.fd(100)
field.bk(150)
field.penup()
field.left(90)
field.fd(50)
field.pendown()
field.right(90)
field.fd(150)

screen.listen()

game_is_on = True
NUM_OF_CELLS = 0

# two grids: 1 to cross, another to use coordinates for cross line animation
grid = [
        [-50, 50],
        [0, 50],
        [50, 50],
        [-50, 0],
        [0, 0],
        [50, 0],
        [-50, -50],
        [0, -50],
        [50, -50]
    ]

grid2 = [
        [-50, 50],
        [0, 50],
        [50, 50],
        [-50, 0],
        [0, 0],
        [50, 0],
        [-50, -50],
        [0, -50],
        [50, -50]
    ]


# Cross line animation function
def cross_line(x, y, a, b):
    line = Turtle()
    line.hideturtle()
    line.penup()
    line.goto(x, y)
    line.pendown()
    line.goto(a, b)


# To see if there are 3 in a row
def win():
    if grid[0] == grid[1] == grid[2]:
        cross_line(grid2[0][0], grid2[0][1], grid2[2][0], grid2[2][1])
        return True
    elif grid[3] == grid[4] == grid[5]:
        cross_line(grid2[3][0], grid2[3][1], grid2[5][0], grid2[5][1])
        return True
    elif grid[6] == grid[7] == grid[8]:
        cross_line(grid2[6][0], grid2[6][1], grid2[8][0], grid2[8][1])
        return True
    elif grid[0] == grid[3] == grid[6]:
        cross_line(grid2[0][0], grid2[0][1], grid2[6][0], grid2[6][1])
        return True
    elif grid[1] == grid[4] == grid[7]:
        cross_line(grid2[1][0], grid2[1][1], grid2[7][0], grid2[7][1])
        return True
    elif grid[2] == grid[5] == grid[8]:
        cross_line(grid2[2][0], grid2[2][1], grid2[8][0], grid2[8][1])
        return True
    elif grid[0] == grid[4] == grid[8]:
        cross_line(grid2[0][0], grid2[0][1], grid2[8][0], grid2[8][1])
        return True
    elif grid[2] == grid[4] == grid[6]:
        cross_line(grid2[2][0], grid2[2][1], grid2[6][0], grid2[6][1])
        return True
    else:

        return False


def game_over():

    over = Turtle()
    over.penup()
    over.hideturtle()
    over.speed("fastest")
    over.goto(0, 100)
    if win():
        over.write("Winner", align="center", font=("Courtier", 10, "normal"))
    elif not game_is_on:
        over.write("Game over", align="center", font=("Courtier", 10, "normal"))

# To fill the grid
def fill_grid(x, y, player):
    global game_is_on

    if not win() or game_is_on:
        for row in grid:
            if (row[0] == 9 or row[0] == 1) and NUM_OF_CELLS == 8:

                game_is_on = False

            elif x == row[0] and y == row[1]:
                if player == circ:
                    row[0] = 9
                    row[1] = 9
                else:
                    row[0] = 1
                    row[1] = 1
                return True


        else:
            return False


# To fit the circles and crosses inside the cells
def fit(a):
    if a > 0 and a < 25 or a < 0 and a > -25:
        a = 0
    elif a < -25 and a > -75:
        a = -50
    elif a > 25 and a < 75:
        a = 50
    return a


# Warnings when clicking outside the grid
def warning():
    if game_is_on:
        wrong = Turtle()
        wrong.penup()
        wrong.hideturtle()
        wrong.speed("fastest")
        wrong.goto(0, 200)
        wrong.write("Stay withing the grid", align="center", font=("Courtier", 20, "normal"))

        time.sleep(1)
        wrong.clear()

def filled_cell():
    if game_is_on:
        crossed = Turtle()
        crossed.penup()
        crossed.hideturtle()
        crossed.speed("fastest")
        crossed.goto(0, 100)
        crossed.write("Already crossed, try another", align="center", font=("Courtier", 10, "normal"))

        time.sleep(1)
        crossed.clear()



# Draw a circle
def circ(x, y):
    global NUM_OF_CELLS
    if x < -75 or x > 75 or y < -75 or y > 75:

        warning()
    else:
        a = fit(x)
        b = fit(y)

        if fill_grid(a, b, circ) == True:
            o = Turtle()
            o.hideturtle()
            o.speed("fast")
            o.penup()
            o.goto(a, b)
            o.bk(15)
            o.right(90)
            o.pendown()
            o.circle(15)
            NUM_OF_CELLS += 1
        else:
            filled_cell()

# Draw a cross
def cross(x, y):
    global NUM_OF_CELLS
    if x < -75 or x > 75 or y < -75 or y > 75:

        warning()
    else:
        a = fit(x)
        b = fit(y)

        if fill_grid(a, b, cross) == True:
            ex = Turtle()
            ex.hideturtle()
            ex.speed("fast")
            ex.penup()
            ex.goto(a, b)
            ex.right(45)
            ex.bk(15)
            ex.pendown()
            ex.fd(30)
            ex.right(135)
            ex.penup()
            ex.fd(21)
            ex.right(135)
            ex.pendown()
            ex.fd(30)
            NUM_OF_CELLS +=1
        else:
            filled_cell()

# Select randomly who goes first
xo = [cross, circ]
player1 = random.choice(xo)
print(player1)
if player1 == circ:
    player2 = cross
else:
    player2 = circ


# Game
while game_is_on:
    if win():
        game_is_on = False
    else:
        for i in range(9):
            screen.update()

            if i % 2 == 0:
                screen.onclick(player1, btn=1) # Left click of a mouse

            else:
                screen.onclick(player2, btn=3)  # Right click of a mouse


game_over()



screen.mainloop()
