from pathlib import Path
from src.settings import *
import pygame as pg

def load_image(image_path: Path):
    """Load an image and return image object""" 
    try:
        image = pg.image.load(image_path)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except FileNotFoundError:
        print(f'Cannot load image: {image_path}')
        raise SystemExit
    return image, image.get_rect()
