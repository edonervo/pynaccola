import pygame as pg
from src.game import Game
from src.screen import Screen
from src.background import Background
from src.card import Card
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

    # Game Logic
    game = Game() #TODO logic
    card = Card()
    allsprites = pg.sprite.RenderPlain(card)

    #Game loop
    running = True
    while running:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False
        
        allsprites.update(events)
        screen.screen.blit(background.image, (0, 0))
        allsprites.draw(screen.screen)

        pg.display.flip()

        clock.tick(FPS)

    pg.quit()


if __name__ == '__main__':
    main()
