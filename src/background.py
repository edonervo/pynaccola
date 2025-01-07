import pygame as pg
from pathlib import Path

class Background:
    def __init__(
            self, 
            screen: pg.Surface,
            image_path: Path,
            color: tuple|str = (0, 0, 0)
            ):
        """Initialize the background with an image or color"""
        self.color = color
        self.image = pg.image.load(image_path).convert()
        self.screen = screen
        self.image = pg.transform.scale(self.image, self.screen.get_size())

    def render_background(self):
        """Draw the background on the screen"""
        # TODO: add logic to decide between color or image
        # self.screen.fill(self.color)  
        self.screen.blit(self.image, (0, 0))
