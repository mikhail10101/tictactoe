import pygame
from network import Network
import pickle
pygame.font.init()

size = 700
width = size
height = size

window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Tic-Tac-Toe")

def draw(game):

    window.fill((0,0,0))

    pygame.draw.lines(window, (255,255,255), False, [[size//3,0], [size//3,size]],3)
    pygame.draw.lines(window, (255,255,255), False, [[2*size//3,0], [2*size//3,size]],3)
    pygame.draw.lines(window, (255,255,255), False, [[0,size//3], [size,size//3]],3)
    pygame.draw.lines(window, (255,255,255), False, [[0,2*size//3], [size,2*size//3]],3)

    game.draw(window,size)

    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())

    print("You are player", player)

    while run:
        pygame.draw.lines(window, (255,255,255), False, [[0,2*size//3], [size,2*size//3]],3) 

        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        draw(game)

        if (game.check_winner(0) or game.check_winner(1)):
            pygame.time.delay(1000)
            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN and game.connected():
                pos = pygame.mouse.get_pos()
                idx = 3*pos[0]//size
                idy = 3*pos[1]//size
                success = game.play_current_turn(player,idx,idy)
                if (success):
                    n.send(str(player)+":"+str(idx)+":"+str(idy))

main()
