from pathlib import Path
from src.settings import *
import pygame as pg

def load_image(image_path: Path, scale:float = 1.0):
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
    
    size = image.get_size()
    size = (size[0]* scale, size[1]*scale)

    image = pg.transform.scale(image, size)
    return image, image.get_rect()
