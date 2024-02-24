import pygame
import constants

class Scene(object):
    def __init__(self, object):
        self.elements = []
        
    def update(self, events, pressedKeys, mouseState, mousePosition):
        pass
    
    def render(self, surface):
        pass