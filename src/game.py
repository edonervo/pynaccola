import pygame as pg
import pygame as pg
from src.background import Background
from src.cards import Card, CardsDatabase
from src.settings import *
from src.screen import Screen


class Game():
    def __init__(self):
        """
        Initialize the game, setting up the screen, clock, and game state.
        """
        pg.init()

        # Screen
        self.screen = Screen(
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            SCREEN_CAPTION
        )

        # Background
        self.background = Background(
            screen=self.screen.screen,  #TODO: improve
            image_path=BACKGROUND_IMAGE
        )

        # Clock
        self.clock = pg.time.Clock()

        # Game State
        self.running = True

        # Initialize Sprites and Groups
        ## Cards
        cards_db = CardsDatabase()    
        self.card_sprites = pg.sprite.RenderPlain(cards_db.cards)

    def handle_events(self):
        self.events = pg.event.get()
        for event in self.events:
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.running = False

    def update(self, events):   
        self.card_sprites.update(events)
        
    def draw(self):
        self.background.render()
        self.screen.screen.blit(self.background.image, (0, 0))
        self.card_sprites.draw(self.screen.screen)

        pg.display.flip()

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update(self.events)
            self.draw()

            




