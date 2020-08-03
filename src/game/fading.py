__author__ = "Joshua Akangah"

import pygame
from config.settings import *

#screen = pygame.display.set_mode((600, 500))
pygame.init()

class FadingText():
    def __init__(self, text, color, size, fadespeed):
        """
        params:
            text: Text to render
            color: Color to render text in RGB format
            size: Size of text
            fadespeed: Speed at which to fade out text
        return:
            None
        """
        self.text = text
        self.color = color
        self.size = size
        self.speed = fadespeed
        self.font = pygame.font.Font(os.path.join(BASE_DIR, os.path.join("assets","retro.ttf")), self.size)
        self.font1 = pygame.font.Font(os.path.join(BASE_DIR, os.path.join("assets","retro.ttf")), 30)
        self.rendered = None
        self.alpha = 255

    def render(self):
        """
        params: None
        return: None
        Function to set the rendered text
        """
        try:
            self.rendered = self.font.render(f"{self.text}", True, self.color)
        except:
            pass
        #screen.blit(self.rendered, (100,100))

    def fade(self, display, x, y):
        """
        params:
            display: Main display to show the fading text on
            x: X position you want to display text
            y: Y position you want to display text
        """
        try:
            temp = pygame.Surface((self.rendered.get_width(), self.rendered.get_height())).convert()
            temp.blit(display, (-x,-y))
            temp.blit(self.rendered, (0,0))
            if self.alpha > 0:
                temp.set_alpha(self.alpha)
                self.alpha -= self.speed
                display.blit(temp, ((display.get_width()/2)-(temp.get_width()/2), y))
        except:
            pass