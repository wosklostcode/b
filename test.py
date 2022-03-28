# Взято из PR-ветки husano896 (немного изменено)
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()


def main():
   while True:
      for event in pygame.event.get():
            if event.type == QUIT:
               pygame.quit()
               return
            elif event.type == MOUSEWHEEL:
               print(event)
               print(event.x, event.y)
               print(event.flipped)
               print(event.which)
               # может получить доступ к свойствам с помощью
               # правильная запись (например: event.y)
      clock.tick(60)

# Запустить игру:
main()