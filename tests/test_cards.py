import pytest
import pygame as pg
import pandas as pd
from src.cards import Card, CardsDatabase
from pathlib import Path
from src.settings import *
from src.screen import Screen

# Init test
screen = Screen(
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_CAPTION
)

def test_card_init():

    # Given
    rank = '2'
    suit = 'hearts'

    # When
    card = Card(
        rank=rank,
        suit=suit,
        source_file='2_of_hearts.png'
    )

    # Then
    assert card.rank == '2'
    assert card.suit == 'hearts'
    assert card.name == '2 of hearts'
    assert card.value == 5
    assert card.dragging == False
    assert card.image is not None
    assert card.rect is not None

def test_card_database():
    cards_db = CardsDatabase()
    cards = cards_db.cards
    cards_df = pd.DataFrame(
        columns = ['card_name', 'card_rank', 'card_suit', 'card_value', 'card_source'],
        data = [
            [card.name, card.rank, card.suit, card.value, card.source_file.stem] for card in cards.values()
        ]
    )
    cards_df = cards_df.sort_values(by=['card_rank', 'card_suit'])
    print(cards_df.info())



if __name__ == '__main__':
    test_card_init()
    test_card_database()