import pygame
from network import Network
from board import Board

class Player:
    width = height = 30

    def __init__(self,startx, starty, color=(255,0,0)):
        self.x = startx
        self.y = starty
        self.color = color

    def draw(self,g):
        pygame.draw.rect(g, self.color, (self.x,self.y,self.width,self.height),0)

    def move(self, newX, newY):
        self.x = newX
        self.y = newY

class Game:
    def __init__(self,s):
        self.net = Network()

        self.size = s
        self.canvas = Canvas(s, "Testing tic-tac-toe")
        self.board = Board(s)

        self.player = Player(0,0)
        self.player2 = Player(0,0)

    def run(self):
        clock = pygame.time.Clock()
        run = True

        while run:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.K_ESCAPE:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click_loc = pygame.mouse.get_pos()
                        res0 = self.board.findIndex(click_loc[0],click_loc[1])
                        self.player.move(res0[0]*self.size/3,res0[1]*self.size/3)

            p2x, p2y = self.parse_data(self.send_data())
            res1 = self.board.findIndex(p2x,p2y)
            self.player2.move(res1[0]*self.size/3,res1[1]*self.size/3)

            self.canvas.draw_background()
            self.board.draw(self.canvas.get_canvas())
            self.player.draw(self.canvas.get_canvas())
            self.player2.draw(self.canvas.get_canvas())
            self.canvas.update()

        pygame.quit

    def send_data(self):
        data = str(self.net.id) + ":" + str(self.player.x) + "," + str(self.player.y)
        reply = self.net.send(data)
        return reply
    
    @staticmethod
    def parse_data(data):
        try:
            d = data.split(":")[1].split(",")
            return int(d[0]), int(d[1])
        except:
            return 0,0

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