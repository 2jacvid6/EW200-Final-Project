import pygame
from background import Background
from players import Player1
from players import Player2
from players import Ball
from goal import Goal
pygame.init()

TS = 64
SIZE = (13*TS, 9*TS)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

bg = pygame.Surface(SIZE)
bg.fill((100,100,255))

bg_builder = Background(SIZE, TS)
p1 = Player1(256,288)
p2 = Player2(576,288)
ball = Ball(416,288)
goal1 = Goal(0, 3*TS, TS)
goal2 = Goal(12*TS, 3*TS, TS)


running = 1
while running:
    screen.blit(bg, (0,0))
    bg_builder.make_bg()
    bg_builder.draw(bg)
    
    p1.draw(screen)
    p2.draw(screen)
    ball.draw(screen)
    pygame.display.flip()
    
    events = pygame.event.get()
    
    p1.update()
    p2.update()
    
    ball.kick(p1)
    ball.kick(p2)
    ball.update()
    
    goal1.update(ball)
    
    for e in events:
        if e.type == pygame.QUIT:
            running = 0
    
    clock.tick(60)        


pygame.quit()