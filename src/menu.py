import pygame as pg
from enum import Enum


class MenuChoice:
    PLAY = 0

class Menu:
    def __init__(self,
                 screen: pg.Surface,
                 options,
                 font_name='Arial',
                 font_size=36,
                 text_color = (255, 255, 255),
                 selected_color = (255, 0 , 0)
                 ):
        """
        Initialize the menu.

        Args:
            screen (pygame.Surface): The screen where the menu will be displayed.
            options (list): List of menu options as strings.
            font_name (str): Name of the font for menu text.
            font_size (int): Size of the font.
            text_color (tuple): RGB color for non-selected options.
            selected_color (tuple): RGB color for the selected option.
        """
        self.screen = screen
        self.options = options
        self.font = pg.font.Font(pg.font.match_font(font_name), font_size)
        self.text_color = text_color
        self.selected_color = selected_color
        self.current_selection = MenuChoice.PLAY