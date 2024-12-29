import pygame as pg

class Background:
    def __init__(
            self, 
            screen,
            image_path,
            screen_width,
            screen_height,
            color: tuple|str = (0, 0, 0)
            ):
        """Initialize the background with an image or color"""
        self.color = color
        self.image = pg.image.load(image_path).convert()
        self.image = pg.transform.scale(self.image, (screen_width, screen_height))
        self.screen = screen
        self.render()

    def render(self):
        """Draw the background on the screen"""
        # TODO: add logic to decide between color or image
        # self.screen.fill(self.color)  
        self.screen.blit(self.image, (0, 0))
