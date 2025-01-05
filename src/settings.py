from pathlib import Path

# Texts
SCREEN_CAPTION = 'Pinnacola Game'

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Frame rate
FPS = 60

# Asset paths
ASSETS_DIR = Path(__file__).resolve().parent.parent / 'assets'
IMAGES_DIR = ASSETS_DIR / 'images'
CARDS_DIR = ASSETS_DIR / IMAGES_DIR / 'cards'

# Images
BACKGROUND_IMAGE = IMAGES_DIR / 'green-board.jpg'

# Cards data
CARDS_VALUE = {
    "ace": 15, "2": 5, "3": 5, "4": 5, "5": 5, "6": 5, "7": 10, "8": 10,
    "9": 10, "10": 10, "jack": 10, "queen": 10, "king": 10, "joker": 25
}
