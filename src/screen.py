import pygame as pg
from src.settings import *
from src.background import Background
from pathlib import Path


class Screen:
    def __init__(
            self, 
            width: int, 
            height: int, 
            caption: str, 
            # background_color:tuple|str = (0, 0, 0),
            # background_image:Path = None
            ):
        """
        Initialize the game screen.

        Args:
            width (int): Screen width.
            height (int): Screen height.
            caption (str): Window title.
        """
        self.width = width
        self.height = height
        self.caption = caption

        self.screen = pg.display.set_mode((width, height), pg.SCALED)
        pg.display.set_caption(self.caption)

        