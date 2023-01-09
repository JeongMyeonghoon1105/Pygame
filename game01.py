import pygame

pygame.init()

background = pygame.display.set_mode((600, 480))
pygame.display.set_caption("Game 01")

play = True
while play:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False

pygame.quit()