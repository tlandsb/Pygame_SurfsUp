import pygame

pygame.init()

win = pygame.display.set_mode((800, 900))

bg=pygame.image.load('van.jpg')
win.blit(bg, (0, 0))
pygame.display.update()
pygame.time.delay(5000)