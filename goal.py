import pygame
from players import Ball

class Goal(pygame.sprite.Sprite):
    def __init__(self,x,y,ts):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.ts = ts
        self.size = (self.ts, 3*self.ts)
        self.rect = (x,y, self.size)
        self.count1 = 0
        self.count2 = 0
        self.score = 0
        self.goal1_rect = (0, 3*self.ts, 18, 2*self.ts)
        
    def update(self, ball):
        self.ball = ball
        self.ball_rect = self.ball.get_rect()
        collide = pygame.sprite.collide_rect(self, self.ball_rect)
        if collide:
            print("true")