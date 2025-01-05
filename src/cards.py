import pygame as pg
import warnings
from src.utils import *
from src.settings import *

class Card(pg.sprite.Sprite):
    def __init__(self, 
                 rank: str,
                 suit: str,
                 source_file: Path = None,
                 render: bool = True
                 ):
        pg.sprite.Sprite.__init__(self)
        self.suit = suit
        self.rank = rank
        if 'joker' in rank.lower():
            self.name = 'joker'
        else:
            self.name = f'{rank} of {suit}'
        self.source_file = source_file
        self.value = CARDS_VALUE.get(self.rank)
        try:
            self.image, self.rect = load_image(CARDS_DIR / self.source_file, 0.3)
        except:
            warnings.warn(f'Not able to find source image for {self.name}, card cannot be rendered')
        
        # Render 
        if render:
            self.render()

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
        self.cards = {}
        self._load_cards()

    def parse_card_filename(self, filename: str):
        """
        Parses the filename to extract card details (name, suit, rank).

        Args:
            filename (str): The filename (without extension) of the card image.

        Returns:
            tuple: (suit, rank)
        """
        if 'joker' not in filename:
            rank = filename.split('_')[0]
            suit = filename.split('_')[2]
        else:
            rank = 'joker'
            suit = None

        return suit, rank

    def _load_cards(self, directory: Path = CARDS_DIR):
        """Load cards in memory"""
        for file in directory.iterdir():
            if file.suffix.lower() == ".png":
                # Parse card name, suit, and rank from the filename
                suit, rank = self.parse_card_filename(file.stem)
                card = Card(
                    suit=suit,
                    rank=rank,
                    source_file=file
                )
                self.cards[card.name] = card

            else:
                raise FileNotFoundError
            