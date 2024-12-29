import pygame as pg
from src.game import Game
from src.settings import *


def main():
    pg.init()
    # TODO: Check for failed initialization

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.SCALED)
    pg.display.set_caption(SCREEN_CAPTION)

    clock = pg.time.Clock()

    game = Game()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

        screen.fill('green')

        pg.display.flip()

        clock.tick(FPS)

    pg.quit()


if __name__ == '__main__':
    main()
