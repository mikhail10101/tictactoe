import pygame

winners = [
  [[0,0],[0,1],[0,2]],
  [[1,0],[1,1],[1,2]],
  [[2,0],[2,1],[2,2]],
  [[0,0],[1,0],[2,0]],
  [[0,1],[1,1],[2,1]],
  [[0,2],[1,2],[2,2]],
  [[0,0],[1,1],[2,2]],
  [[0,2],[1,1],[2,0]]
]

#0, nothing
#1, player1
#2, player2
class Board:
    def __init__(self,size) -> None:
        self.values = [[0,0,0],[0,0,0],[0,0,0]]
        self.length = size
    
    def check(self,n):
        for i, series in enumerate(winners):
            valid = True
            for coor in series:
                if winners[coor[0]][coor[1]] != n:
                    valid = False
                    break
            if valid:
                return i
        return -1
    
    def update(self,x,y,n):
        self.values[x][y] = n

    def clear(self):
        for i in range(3):
            for j in range(3):
                self.values[i][j] = 0

    def draw(self, screen):
        x = self.length
        pygame.draw.lines(screen, (0,0,0), False, [[x/3,0], [x/3,x]],3)
        pygame.draw.lines(screen, (0,0,0), False, [[2*x/3,0], [2*x/3,x]],3)
        pygame.draw.lines(screen, (0,0,0), False, [[0,x/3], [x,x/3]],3)
        pygame.draw.lines(screen, (0,0,0), False, [[0,2*x/3], [x,2*x/3]],3)

    def findIndex(self,x,y):
        return [int(x*3/self.length),int(y*3/self.length)]