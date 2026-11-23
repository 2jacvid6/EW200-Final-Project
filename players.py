import pygame
from math import atan2, cos, sin

class Player1(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.fp = r"kenney_sports-pack\PNG\Blue\characterBlue (3).png"
        self.image = pygame.image.load(self.fp)
        self.og_image = pygame.image.load(self.fp)
        self.left_image = pygame.image.load(self.fp)
        self.left_image = pygame.transform.rotate(self.left_image, 180)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.theta = 0
        self.left = False
        
    def draw(self, screen):
        self.rect = self.image.get_rect(center = (self.x,self.y))
        screen.blit(self.image, self.rect)
        
    def check_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.dy -= 3
        elif keys[pygame.K_a]:
            self.dx -= 3
            self.left = True
        elif keys[pygame.K_s]:
            self.dy += 3
        elif keys[pygame.K_d]:
            self.dx += 3
            self.left = False
    
    def update(self):
        self.check_keys()
        self.x += self.dx
        self.y += self.dy
        if self.x <= 0:
            self.x += 5
        elif self.x >= (13*64):
            self.x -= 5
        if self.y <= 0:
            self.y += 5
        elif self.y >= (9*64):
            self.y -= 5
        self.rect.center = (self.x, self.y)
        self.dx = 0
        self.dy = 0
        if self.left:
            self.image = self.left_image
        else:
            self.image = self.og_image

class Player2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.fp = r"kenney_sports-pack\PNG\Red\characterRed (3).png"
        self.image = pygame.image.load(self.fp)
        self.og_image = pygame.image.load(self.fp)
        self.left_image = pygame.image.load(self.fp)
        self.left_image = pygame.transform.rotate(self.left_image, 180)
        self.x = x
        self.y = y
        self.theta = 180
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.dx = 0
        self.dy = 0
        self.right = False

        
    def draw(self, screen):
        self.rect = self.image.get_rect(center = (self.x,self.y))
        screen.blit(self.image, self.rect)
        
        
    def check_keys(self):
        keys2 = pygame.key.get_pressed()
        if keys2[pygame.K_UP]:
            self.dy -= 3
        elif keys2[pygame.K_LEFT]:
            self.dx -= 3
            self.right = False
        elif keys2[pygame.K_DOWN]:
            self.dy += 3
        elif keys2[pygame.K_RIGHT]:
            self.dx += 3
            self.right = True
    
    def update(self):
        self.check_keys()
        self.x += self.dx
        self.y += self.dy
        if self.x <= 0:
            self.x += 5
        elif self.x >= (13*64):
            self.x -= 5
        if self.y <= 0:
            self.y += 5
        elif self.y >= (9*64):
            self.y -= 5
        self.rect.center = (self.x, self.y)
        self.dx = 0
        self.dy = 0
        if self.right:
            self.image = self.og_image
        else:
            self.image = self.left_image
            

class Ball(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.fp = r"kenney_sports-pack\PNG\Equipment\ball_soccer4.png"
        self.image = pygame.image.load(self.fp)
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.theta = 0
        self.image = pygame.transform.rotate(self.image, self.theta)
        self.image = pygame.transform.rotozoom(self.image, 0, 1.5)
        self.rect = self.image.get_rect()
        self.r = 12 #ball is 18 pixels, but radius is times 1.5
        self.acc = 6
    
    def draw(self, screen):
        self.rect = self.image.get_rect(center = (self.x,self.y))
        screen.blit(self.image, self.rect)
        
    def kick(self, player):
        x_pos = max(player.rect.left, min(self.x, player.rect.right))
        y_pos = max(player.rect.top, min(self.y, player.rect.bottom))
        
        x_dist = abs(self.x - x_pos)
        y_dist = abs(self.y - y_pos)
        dist = ((x_dist)**2 + (y_dist)**2)**0.5
        
        if dist <= self.r:
            deltax = self.x - player.rect.centerx
            deltay = self.y - player.rect.centery
            
            phi = atan2(-deltay, deltax)
            
            self.dx += cos(phi) * self.acc
            self.dy -= sin(phi) * self.acc
        
    def update(self):
        self.x += self.dx
        self.y += self.dy
        
        self.dx -= 0.1 * self.dx
        self.dy -= 0.1 * self.dy
        
        if self.x - self.r <= 0:
            self.x = self.r
            self.dx = -self.dx
        elif self.x + self.r >= (13*64):
            self.x = (13*64) - self.r
            self.dx = -self.dx
            
        if self.y - self.r <= 0:
            self.y = self.r
            self.dy = -self.dy
        elif self.y + self.r >= (9*64):
            self.y = (9*64) - self.r
            self.dy = -self.dy
        
        self.rect.center = (self.x, self.y)