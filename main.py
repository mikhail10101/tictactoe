import pygame
from board import Board

pygame.init()

length = 500

canvas = pygame.display.set_mode((length,length))
pygame.display.set_caption("My Board")

exit = False
field = Board(length)

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    canvas.fill((255,255,255))
    field.draw(canvas)
    pygame.display.update()

