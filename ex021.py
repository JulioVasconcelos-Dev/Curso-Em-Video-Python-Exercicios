import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("C:\Users\Júlio Vasconcelos\Downloads\Meus beats\hihat bom.mp3")

pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(1)