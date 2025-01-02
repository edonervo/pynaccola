import pygame as pg
from src.game import Game
from src.screen import Screen
from src.background import Background
from src.settings import *


def main():
    pg.init()
    # TODO: Check for failed initialization

    screen = Screen(
        SCREEN_WIDTH, 
        SCREEN_HEIGHT, 
        'Pynnacola'
    )
    
    background = Background(
        screen=screen.screen,
        image_path=BACKGROUND_IMAGE
    )

    background.render()

    clock = pg.time.Clock()

    game = Game()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

        pg.display.flip()

        clock.tick(FPS)

    pg.quit()


if __name__ == '__main__':
    main()
