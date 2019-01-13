##Template for a page
import pygame
import components.common

from components.common import coordToPixel, isInt, isAdjacent, Node

def GameOver(root):
  pygame.init()
  
  background = (0, 0, 0)

  display_width = 1920
  display_height = 1080

  #Set GUI Size and title
  gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
  pygame.display.set_caption('Pirates PC!')
  clock = pygame.time.Clock()

  #Check for events
  while root.page=="GameOver":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()

        #Monitor when keyboard key is pressed
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()

    winner = root.allShips[0].owner
    gameDisplay.fill(background)
    font = pygame.font.SysFont("Arial", 70, True)
    text = font.render("Congratulations, " + str(winner) + "! You win!", True, [255, 255, 255], None)
    gameDisplay.blit(text, coordToPixel((9,8), root.gridWidth))
    pygame.display.update()