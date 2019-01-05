##This is a testing page for debugging code and testing methods 
import pygame
import common

from common import coordToPixel, isInt, isAdjacent, Node

def run_game():
  pygame.init()
  
  background = (51, 70, 242)
  battlefieldBackground=pygame.image.load('./resources/images/background-battlefield.jpg')

  display_width = 1920
  display_height = 1080

  #Set GUI Size and title
  gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
  pygame.display.set_caption('Pirates PC!')
  clock = pygame.time.Clock()

  #Check for events
  while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()

        #Monitor when keyboard key is pressed
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()

    gameDisplay.fill(background)
    gp_width = pygame.font.SysFont("Arial", 70, True).render("Testing", True, [0, 0, 0], None)
    gameDisplay.blit(gp_width, (0,0))
    pygame.display.update()

run_game()