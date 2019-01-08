##This is a testing page for debugging code and testing methods 
import pygame
import components.common
import components.StateClass

from components.StateClass import State
from components.common     import coordToPixel, isInt, isAdjacent, Node

def main_menu(root):
  # pygame.init()
  
  # background = (51, 70, 200)
  blue  = [0,200,200]
  green = [0,255,0]
  anchor = pygame.image.load('./resources/images/Anchor.png')
  menuBackground = pygame.image.load('./resources/images/menu-background.jpg')
  display_width = 1920
  display_height = 1080

  #Set GUI Size and title
  gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
  pygame.display.set_caption('Pirates PC!')
  clock = pygame.time.Clock()

  #Check for events
  while root.page == "Menu":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()

        #Monitor when keyboard key is pressed
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
        
        #Left mouse button is clicked
        if (pygame.mouse.get_pressed()[0] == 1) and root.select == "Play":
          root.page = "Play"
        if (pygame.mouse.get_pressed()[0] == 1) and root.select == "Quit":
          pygame.quit()
          exit()

    #monitor mouse location
    mx, my = pygame.mouse.get_pos()
    if mx >= 100 and mx < 240 and my > 600 and my < 690:
      root.select = "Play" 
    elif mx >= 100 and mx < 240 and my > 700 and my < 790:
      root.select = "Quit"
    else:
      root.select = False

    #render background
    gameDisplay.blit(menuBackground, (0,0))
    
    #render words
    font = pygame.font.SysFont("Arial", 70, True)
    play = font.render("Play", True, (blue, green)[root.select == "Play"], None)
    quit = font.render("Quit", True, (blue, green)[root.select == "Quit"], None)
    gameDisplay.blit(play, (100, 600))
    gameDisplay.blit(quit, (100, 700))
    if root.select == "Play":
      gameDisplay.blit(anchor, (25, 610))
    elif root.select == "Quit":
      gameDisplay.blit(anchor, (25, 710))

    #update gui
    pygame.display.update()