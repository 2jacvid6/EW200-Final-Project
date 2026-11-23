import pygame

class Background:
    def __init__(self, size, ts):
        self.size = size
        self.ts = ts
        self.tilemap = pygame.image.load(r"kenney_sports-pack\Tilesheet\groundGrass_mownWide.png")
        self.tilemap2 = pygame.image.load(r"kenney_sports-pack\Tilesheet\elements.png")
        g = (0,0,self.ts,self.ts)
        g_btlc = (self.ts, 0, self.ts, self.ts)
        g_btrc = (5*self.ts, 0, self.ts, self.ts)
        g_bblc = (self.ts, 2*self.ts, self.ts, self.ts)
        g_bbrc = (4*self.ts, 3*self.ts, self.ts, self.ts)
        g_ts = (2*self.ts, 0, self.ts,self.ts)
        g_bs = (2*self.ts, 3*self.ts, self.ts, self.ts)
        g_rs = (4*self.ts, self.ts, self.ts, self.ts)
        g_ls = (self.ts, self.ts, self.ts, self.ts)
        g_hl = (3*self.ts, self.ts, self.ts, self.ts)
        g_half = (2*self.ts, self.ts, self.ts, self.ts)
        g_tlc = (5*self.ts, 0, self.ts, self.ts)
        g_trc = (6*self.ts, 0, self.ts, self.ts)
        g_blc = (5*self.ts, self.ts, self.ts, self.ts)
        g_brc = (6*self.ts, self.ts, self.ts, self.ts)
        g_tsh = (3*self.ts,0,self.ts,self.ts)
        g_bsh = (3*self.ts,3*self.ts,self.ts,self.ts)
        self.goal = (6*self.ts + 18, 3*self.ts, self.ts, self.ts)
        self.goal2 = (6*self.ts + 18, 4*self.ts, self.ts, self.ts)
        self.goal3 = (6*self.ts + 18, 5*self.ts, self.ts, self.ts)
        self.goal4 = (7*self.ts - 18, 3*self.ts, self.ts, self.ts)
        self.goal5 = (7*self.ts - 18, 4*self.ts, self.ts, self.ts)
        self.goal6 = (7*self.ts - 18, 5*self.ts, self.ts, self.ts)
        
        self.tile_matrix = [
                [g_tlc,g_ts,g_ts,g_ts,g_ts,g_ts,g_tsh,g_ts,g_ts,g_ts,g_ts,g_ts,g_trc],
                [g_ls, g,g,g,g,g,g_hl,g,g,g,g,g,g_rs ],
                [g_ls, g,g,g,g,g,g_hl,g,g,g,g,g,g_rs ],
                [g_ls, g,g,g,g,g,g_hl,g,g,g,g,g,g_rs ],
                [g_ls, g,g,g,g,g,g_hl,g,g,g,g,g,g_rs ],
                [g_ls, g,g,g,g,g,g_hl,g,g,g,g,g,g_rs ],
                [g_ls, g,g,g,g,g,g_hl,g,g,g,g,g,g_rs ],
                [g_ls, g,g,g,g,g,g_hl,g,g,g,g,g,g_rs ],
                [g_blc,g_bs,g_bs,g_bs,g_bs,g_bs,g_bsh,g_bs,g_bs,g_bs,g_bs,g_bs,g_brc]
            ]
    def make_bg(self):
        self.bg = pygame.Surface(self.size)
        for r in range(len(self.tile_matrix)):
            for c in range(len(self.tile_matrix[r])):
                self.bg.blit(self.tilemap, (c*self.ts, r*self.ts), self.tile_matrix[r][c])
        self.bg.blit(self.tilemap2, (0, 3*self.ts), self.goal)
        self.bg.blit(self.tilemap2, (0, 4*self.ts), self.goal2)
        self.bg.blit(self.tilemap2, (0, 5*self.ts), self.goal3)
        self.bg.blit(self.tilemap2, (12*self.ts, 3*self.ts), self.goal4)
        self.bg.blit(self.tilemap2, (12*self.ts, 4*self.ts), self.goal5)
        self.bg.blit(self.tilemap2, (12*self.ts, 5*self.ts), self.goal6)
        self.rect = self.bg.get_rect()
        return self.bg
    
    def draw(self, screen):
        self.screen = screen
        self.screen.blit(self.bg, self.rect)