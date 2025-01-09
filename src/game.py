import pygame as pg
import pygame as pg
from src.background import Background
from src.cards import Card, CardsDatabase
from src.settings import *
from src.screen import Screen
from src.menu import Menu
from enum import Enum

class GameState(Enum):
    MENU = 0
    GAMEPLAY = 1
    PAUSE = 2
    GAME_OVER = 3

class GameStateManager:
    def __init__(self):
        self.current_state = GameState.MENU


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
        self.game_state = GameState.MENU

        # Menu
        self.menu = Menu(
            self.screen.screen,
            MENU_OPTIONS
        )

        # Initialize Sprites and Groups
        ## Cards
        cards_db = CardsDatabase()    
        self.card_sprites = pg.sprite.RenderPlain(cards_db.cards['joker'])

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.handle_events()
            self.update(self.events)
            self.render()

    def handle_events(self):
        self.events = pg.event.get()
        for event in self.events:
            if event.type == pg.QUIT:
                self.quit_game()                

    def update(self, events):
        if self.game_state == GameState.MENU:
            self.menu.update(events)
        elif self.game_state == GameState.GAMEPLAY:
            self.card_sprites.update(events)
        else:
            pass
        
    def render(self):
        self.background.render_background()
        self.screen.screen.blit(self.background.image, (0, 0))
        if self.game_state == GameState.MENU:
            self.render_menu()
        if self.game_state == GameState.GAMEPLAY:
            self.card_sprites.draw(self.screen.screen)

        pg.display.flip()

    def render_menu(self):
        self.menu.render()

    def main_menu(self):
        """
        Display the main menu
        """
        pass

    def quit_game(self):
        """
        Quits the game
        """
        pg.quit()
        quit()


            




