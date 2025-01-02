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

    def update(self):
        pass