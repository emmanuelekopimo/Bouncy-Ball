from string import ascii_letters
import string
import pygame.locals

ABC = list(ascii_letters)
NUMBERS = list(string.digits)

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 660

MAX_BAT_WIDTH = 170
MAX_BAT_DISPLACEMENT = MAX_BAT_WIDTH/2
BLOCK_WIDTH = 20
BLOCK_HEIGHT = 20

PLAYING = 1
FAILED = 2
WON = 3

ADD3 = 1
ADD5 = 2
MULTIPLY3 = 3
MULTIPLY5 = 4
ADDLIFE = 5