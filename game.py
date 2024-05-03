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

class Game:
    def __init__(self, id):
        self.id = id
        self.ready = False
        self.turns = 0
        self.values = [
            [-1,-1,-1],
            [-1,-1,-1],
            [-1,-1,-1]
        ]
        self.mode = 0
    
    #return true on success, false on failure
    def play_current_turn(self, p, x, y):
        if ((self.turns + self.mode//2)%2 != p):
            return False
        if self.values[x][y] != -1:
            return False
        self.values[x][y] = p
        self.turns += 1
        return True

    def connected(self):
        return self.ready

    #return -1, 0, or 1
    def check_winner(self, p):
        for series in winners:
            won = True
            for s in series:
                won = won and (self.values[s[0]][s[1]] == p)
            if (won): return True
        return False

    def reset(self):
        self.turns = 0
        self.values = [
            [-1,-1,-1],
            [-1,-1,-1],
            [-1,-1,-1]
        ]
        self.mode = (self.mode+1)%4

    def draw(self, win, size):
        for i in range(3):
            for j in range(3):
                if self.values[i][j] == 1:
                    pygame.draw.lines(win, (255,255,255), False, [[i*(size//3),j*(size//3)], [(i+1)*(size//3),(j+1)*(size//3)]],3)
                    pygame.draw.lines(win, (255,255,255), False, [[(i+1)*(size//3),j*(size//3)], [i*(size//3),(j+1)*(size//3)]],3)
                elif self.values[i][j] == 0:
                    pygame.draw.circle(win, (255,255,255), [(2*i+1)*(size//3)//2, (2*j+1)*(size//3)//2], size*0.8//6)