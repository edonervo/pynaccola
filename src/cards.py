import pygame as pg
from src.utils import *
from src.settings import *

class Card(pg.sprite.Sprite):
    def __init__(self, 
                 name: str,
                 suit: str,
                 rank: str
                 ):
        pg.sprite.Sprite.__init__(self)
        self.name = name
        self.suit = suit
        self.rank = rank
        self.value = CARDS_VALUE.get(self.rank)
        self.image, self.rect = load_image(CARDS_DIR / self.name, 0.3)
        self.dragging = False

    def update(self, events):
        """
        Update the card sprite's position based on mouse events.

        Args:
            events (list): List of Pygame events.
        """
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.dragging = True
                    self.mouse_offset = (
                        self.rect.x - event.pos[0],
                        self.rect.y - event.pos[1]  
                    )

            elif event.type == pg.MOUSEBUTTONUP:
                self.dragging = False
            
            elif event.type == pg.MOUSEMOTION:
                if self.dragging:
                    self.rect.x = event.pos[0] + self.mouse_offset[0]
                    self.rect.y = event.pos[1] + self.mouse_offset[1]

    def render(self):
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.rect.center = self.area.center
        self.dragging = False


class CardsDatabase:
    def __init__(self):
        """
        A database to manage all card data of the French Deck
        """
        self.cards = []
        self._load_cards()

    def parse_card_filename(self, filename: str):
        """
        Parses the filename to extract card details (name, suit, rank).

        Args:
            filename (str): The filename (without extension) of the card image.

        Returns:
            tuple: (name, suit, rank)
        """
        if 'joker' not in filename:
            rank = filename.split('_')[0]
            suit = filename.split('_')[1]
            name = f'{rank} of {suit}'
        else:
            rank = 'joker'
            suit = None
            name = 'Joker'

        return name, suit, rank

    def _load_cards(self, directory: Path = CARDS_DIR):
        """Load cards in memory"""
        for file in directory.iterdir():
            if file.suffix.lower() == ".png":
                # Parse card name, suit, and rank from the filename
                name, suit, rank = self.parse_card_filename(file.stem)
                card = Card(
                    name=name,
                    suit=suit,
                    rank=rank
                )
                self.cards.append(card)

            else:
                raise FileNotFoundError
            