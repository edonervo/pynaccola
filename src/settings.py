from pathlib import Path

#Texts
SCREEN_CAPTION = 'Pinnacola Game'

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Frame rate
FPS = 60

# Asset paths
ASSETS_DIR = Path(__file__).resolve().parent.parent / 'assets'
IMAGES_DIR = ASSETS_DIR / 'images'

# Images
BACKGROUND_IMAGE = IMAGES_DIR / 'black-board.jpg'