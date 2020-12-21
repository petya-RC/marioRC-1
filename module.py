import os
import pygame


def print_text (text, x, y, color, win, size, font_type='D:\GAME_MARIO\Pixel_Sans_Serif.ttf'):
    font_type = pygame.font.Font(font_type, size)
    text = font_type.render(text, True, color)
    win.blit(text, (x, y))

def gribchek(xMin, xMax, yMin, yMax, x, y, statusB, score):
    if x >= xMin and x <= xMax and y <= yMin and y >= yMax:
        statusB = True
        score += 100
    
