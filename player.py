import pygame

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