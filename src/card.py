import pygame as pg
from src.utils import *
from src.settings import *

class Card(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(CARDS_DIR / '2_of_clubs.png', 0.3)
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.rect.center = self.area.center
        self.dragging = False

    def update(self, events):
        """
        Update the sprite's position based on mouse events.

        Args:
            events (list): List of Pygame events.
        """
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.dragging = True
                    self.mouse_offset = (
                        self.rect.x - event.pos[0],
                        self.rect.y - event.pos[1]  
                    )

            elif event.type == pg.MOUSEBUTTONUP:
                self.dragging = False
            
            elif event.type == pg.MOUSEMOTION:
                if self.dragging:
                    self.rect.x = event.pos[0] + self.mouse_offset[0]
                    self.rect.y = event.pos[1] + self.mouse_offset[1]