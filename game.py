import pygame
from network import Network
from board import Board
from player import Player

class Game:
    def __init__(self,s):
        self.net = Network()

        self.size = s
        self.canvas = Canvas(s, "Testing tic-tac-toe")
        self.board = Board(s)


    def run(self):
        clock = pygame.time.Clock()
        run = True

        p = self.net.getId()

        while run:
            p2 = self.net.send(p)
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.K_ESCAPE:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click_loc = pygame.mouse.get_pos()
                        resx = int(int(click_loc[0]*3/self.size) * self.size/3)
                        resy = int(int(click_loc[1]*3/self.size) * self.size/3)
                        self.player.move(resx,resy)

            self.canvas.draw_background()
            self.board.draw(self.canvas.get_canvas())
            p.draw(self.canvas.get_canvas())
            p2.draw(self.canvas.get_canvas())
            self.canvas.update()

        pygame.quit

class Canvas:
    def __init__(self,size,name="None"):
        self.width = size
        self.height = size
        self.screen = pygame.display.set_mode((size,size))
        pygame.display.set_caption(name)

    @staticmethod
    def update():
        pygame.display.update()

    def get_canvas(self):
        return self.screen
    
    def draw_background(self):
        self.screen.fill((255,255,255))