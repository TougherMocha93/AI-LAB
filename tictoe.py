import numpy as np
import pygame

#Prerequisites!

rows = 3
columns = 3
#pygame prerequisites

window_size = (600,600)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
rad = 50

points = [[(100, 100), (100, 300), (100, 500)], [(300, 100), (300, 300), (300, 500)], [(500, 100), (500, 300), (500, 500)]]
rounds = [100,300,500]

board = np.zeros((rows,columns))

game_status = True
Turn = 0

#Game Functions!

def closest(K):
     lst = np.asarray(rounds)
     idx = (np.abs(lst - K)).argmin()
     return lst[idx]

def mark(row,col,player):
    board[row][col] = player

def board_is_full():
    for r in range(rows):
        for c in range(columns):
            if board[r][c] == 0:
                return False
    return True

def mark_valid(r,c):
    if board[r][c] == 0:
        return True
    return False

def endgame(pl):
    global game_status
    print(f"Player {pl} has won the match!")
    pygame.time.wait(3000)
    game_status = False
    

def check_win(player):
    for r in range(rows):
        if board[r][0] == board[r][1] == board[r][2] == player:
            return True
    for c in range(columns):
        if board[0][c] == board[1][c] == board[2][c] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[2][0] == board[1][1] == board[0][2] == player:
        return True

player = 0

def pygame_setup():
    window.fill(white)
    lines = [[(200, 0), (200, 600)], [(400, 0), (400, 600)], [(0, 200), (600, 200)], [(0, 400), (600, 400)]] 
    for i in lines:
        pygame.draw.line(window,black,i[0],i[1],5)

def circle(row,column,player):
    if player == 1:
        color = red
    else:
        color = blue
    pygame.draw.circle(window,color,points[row][column],rad,5)

def cross(row,column,player):
    if player == 1:
        color = red
    else:
        color = blue
    center = points[row][column]
    x = center[0]
    y = center[1]
    pygame.draw.line(window,color,(x-rad,y+rad),(x+rad,y-rad),5)
    pygame.draw.line(window,color,(x+rad,y+rad),(x-rad,y-rad),5)     

#THE GAME!!!

pygame.init()
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Tic-Tac-Toe")
pygame_setup()
pygame.display.update()

while game_status is True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    dict = { 1 : 0 , 3 : 1 , 5 : 2}
        
    if event.type == pygame.MOUSEBUTTONDOWN:
        if Turn % 2 == 0:
            
            #Player1's turn (X)
            
                x = event.pos[0]
                y = event.pos[1]
                row = dict[int(round(closest(x) / 100))]
                col = dict[int(round(closest(y) / 100))]
                

                if not mark_valid(row,col):
                    #print('\nInvalid Move! Try again.')
                    print("",end="")
                else:
                    print(f"{row},{col},Player 1")
                    mark(row,col,1)
                    cross(row,col,1)
                    pygame.display.update()
                    Turn += 1
                
        else:
            #Player2's turn (O)
            
                x = event.pos[0]
                y = event.pos[1]
                row = dict[int(round(closest(x) / 100))]
                col = dict[int(round(closest(y) / 100))]

                if not mark_valid(row,col):
                    #print('\nInvalid Move! Try again.')
                    print("",end="")
                else:
                    print(f"{row},{col},Player 2")
                    mark(row,col,2)
                    circle(row,col,2)
                    pygame.display.update()
                    Turn += 1

    if board_is_full():
        print("Game Over! Tie!")
        game_status = False
    
    if check_win(1):
                endgame(1)

    if check_win(2):
                endgame(2)