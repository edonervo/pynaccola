import pygame as pg
from enum import Enum


class Menu:
    def __init__(self,
                 screen: pg.Surface,
                 options: list[str],
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
        self.current_selection = 0

    def render(self):
        """
        Render the Menu on the screen
        """
        menu_width, menu_height = self.screen.get_size()
        total_height = len(self.options) * self.font.get_height()

        for i, option in enumerate(self.options):
            color = self.selected_color if i == self.current_selection else self.text_color
            text_surface = self.font.render(option, True, color)
            text_rect = text_surface.get_rect(center=(menu_width // 2, (menu_height // 2 - total_height // 2) + i * self.font.get_height()))
            self.screen.blit(text_surface, text_rect)

    def update(self, events: list[pg.event.Event]):
        """
        Update the Menu based on user input
        """
        for event in events:
            if event.type == pg.KEYDOWN:
                print('KEYDOWN')
                if event.type == pg.K_UP:
                    print('KEYUP')
                    self.current_selection = (self.current_selection - 1) % len(self.options)
                elif event.type == pg.K_DOWN:
                    print('KEYUP')
                    self.current_selection = (self.current_selection + 1) % len(self.options)
                elif event.key == pg.K_RETURN:
                    print('KEYRETURN')
                    return self.options[self.current_selection] 
            

