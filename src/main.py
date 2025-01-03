import pygame as pg
from src.game import Game
from src.background import Background
from src.card import Card
from src.settings import *


def main():
    pg.init()
    # TODO: Check for failed initialization

    game = Game()

    while game.running:
        game.run()
    pg.quit()


if __name__ == '__main__':
    main()
