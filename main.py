
# Importing Sys and Pygame
import sys, pygame as pg
pg.init() 

screen_size = 680, 680 
pg.display.set_caption("Binary Search") 
# Creating the Screen 

screen = pg.display.set_mode(screen_size)
font = pg.font.SysFont(None, 80) 

# Setting RGB values for the colors
RED = (255, 0, 0) 
GREEN = (0, 255, 0)
BLUE = (0, 0, 255) 
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0) 
TURQUOISE = (64, 224, 208) 
 
# Setting the width and height of the grid
WIDTH = 70
HEIGHT = 70
 
# Margin between the cells
MARGIN = 5
 
# Creating the number grid
number_grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9], 
[10, 11, 12, 13, 14, 15, 16, 17, 18], 
[19, 20, 21, 22, 23, 24, 25, 26, 27], 
[28, 29, 30, 31, 32, 33, 34, 35, 36], 
[37, 38, 39, 40, 41, 42, 43, 44, 45], 
[46, 47, 48, 49, 50, 51, 52, 53, 54], 
[55, 56, 57, 58, 59, 60, 61, 62, 63], 
[64, 65, 66, 67, 68, 69, 70, 71, 72], 
[73, 74, 75, 76, 77, 78, 79, 80, 81]]
# Creating the visualizer grid 
grid = []
for row in range(9):
    grid.append([])
    for column in range(9):
        grid[row].append(0)  
 

 
# Drawing the Grid
def draw_grid(): 
    for row in range(9):
        for column in range(9):
            color = BLACK
            # Colorcoding the grid
            # Orange represents the low, high, and mid values
            if grid[row][column] == 2:
                color = ORANGE
            pg.draw.rect(screen,color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
            # Red represents the target value, the user decided to pick. 
            if grid[row][column] == 3: 
                color = RED
                pg.draw.rect(screen,color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
            # Blue represents the values the algorithmn passed in order to get to either the target value.
            if grid[row][column] == 4: 
                color = BLUE 
                pg.draw.rect(screen,color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])      
            # Turquoise represents the value of the mid in 1-5 or 5-9.          
            if grid[row][column] == 5: 
                color = TURQUOISE
                pg.draw.rect(screen,color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])                


# Drawing the number grid to the grid. 
def draw_numbers(): 
    row = 0 
    while row < 9: 
            col = 0 
            while col < 9: 
                for i in number_grid: 
                    output = number_grid[row][col]
                    number_text = font.render(str(output), True, pg.Color('GREEN')) 
                    screen.blit(number_text, pg.Vector2((col * 80) + 0, (row * 80) + 5))
                    
                    col += 1 

            row += 1 


 
# The Binary Search Algorithmn
def binarySearch(number_grid, x, low, high): 
    while low <= high: 
        mid = (0 + 8)//2
        row = pos[1] // (HEIGHT + MARGIN)
        trueTarget = pos[0] // (WIDTH + MARGIN)
        # Gathers the distance beteen the low value and mid value. 
        lowDifference = number_grid[row][mid] - number_grid[row][low]  
        # Gathers the distance between the high value and mid value
        highDifference = number_grid[row][high] - number_grid[row][mid]
        # If the target the user chooses is equal to the mid value.
        if number_grid[row][mid] == x: 
            # Setting the low and high values to ORANGE
            grid[row][low] = 2
            grid[row][high] = 2
            # While the difference between mid and low value is greater than 1, iterate until the values between 1-5 that are not low, lowmid or mid values, are blue and have been passed.
            while lowDifference > 1: 
                lowDifference -= 1 
                grid[row][lowDifference ] = 4
            # While the difference between high and mid value is less than 7, iterate until the values between 5-9 that are not mid, highmid or high values, are blue.

            while highDifference < 7: 
                highDifference += 1 
                grid[row][highDifference] = 4 
            grid[row][mid] = 3   

            return mid
        if number_grid[row][mid] > x:
            grid[row][mid] = 2 
            grid[row][low] = 2
            lowmid = 2
            while lowDifference > 1: 
                lowDifference -= 1 
                grid[row][lowDifference ] = 4
            grid[row][trueTarget] = 3 
            grid[row][lowmid] = 5
            
            return lowmid
        else:
            grid[row][mid] = 2 
            highmid = 6
            while highDifference < 8: 
                highDifference += 1 
                grid[row][highDifference] = 4 
                grid[row][high] = 2 
            grid[row][trueTarget] = 3 

            grid[row][highmid] = 5 
            return highmid
    return -1

 

clock = pg.time.Clock()
 

def main_loop(): 
    for event in pg.event.get():  
        if event.type == pg.QUIT:  
            sys.exit() 
        elif event.type == pg.MOUSEBUTTONDOWN:
            # User gets the position of the mouse 
            global pos 
            pos = pg.mouse.get_pos()
            # Changing the x/y coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Setting the location, the user chooses equal to one
            grid[row][column] = 3
            target = number_grid[row][column] 
            binarySearch(number_grid, target, 0, len(number_grid)-1)

    # Set the screen background
    screen.fill(GREEN)
 
    # Draws grid and draws the numbers to the grid 
    draw_grid() 
    draw_numbers() 
    

   

 
    clock.tick(30)
 
    # Update the screen
    pg.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
while 1: 
    main_loop() 
