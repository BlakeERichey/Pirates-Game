##Template for a page
import pygame
import components.common, components.BasicObject
from components.BasicObject import BasicObject
from components.common import coordToPixel, isInt, isAdjacent, Node, pixelToCoord

def Setup(root):
  pygame.init()
  state = BasicObject()

  background = (51, 70, 242)
  cargo=pygame.image.load('./resources/images/Icon_Cargo.png')
  galley=pygame.image.load('./resources/images/Icon_Galley.png')
  schooner=pygame.image.load('./resources/images/Icon_Schooner.png')
  battlefieldBackground=pygame.image.load('./resources/images/background-battlefield.jpg')

  display_width = 1920
  display_height = 1080

  #Set GUI Size and title
  gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
  pygame.display.set_caption('Pirates PC!')
  clock = pygame.time.Clock()

  #Check for events
  while root.page=="Setup":

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
      if (pygame.mouse.get_pressed()[0] == 1):
        print("Button Click")
        mx, my = pygame.mouse.get_pos()
        if mx >= 480 and mx < 530 and my > 280 and my < 330:
          print("I am here.")
          state.addShip("Schooner")
          print(state.schoonerQty)
        if mx >= 250 and mx < 285 and my > 300 and my < 320:
          print("I am here.")
          state.subShip("Schooner")
          print(state.schoonerQty)
      
        
          
             

    gameDisplay.fill(background)
    gameDisplay.blit(battlefieldBackground, (0,0))

    #Define text
    font        = pygame.font.SysFont("Arial", 70, True)
    subtract    = font.render("–", True, [0, 0, 0], None)
    cargoQty    = font.render(str(state.cargoQty), True, [0, 0, 0], None)
    galleyQty   = font.render(str(state.galleyQty), True, [0, 0, 0], None)
    schoonerQty = font.render(str(state.schoonerQty), True, [0, 0, 0], None)
    addition    = pygame.font.SysFont("Arial", 80, True).render("  +", True, [0, 0, 0], None)
    pointsLeft  = font.render("Points Left: " + str(state.pointsLeft), True, [0, 0, 0], None)

    #Render text
    gameDisplay.blit(pointsLeft, (700,0))
    gameDisplay.blit(cargoQty, (1500, 437))
    gameDisplay.blit(galleyQty, (1500, 636))
    gameDisplay.blit(schoonerQty, (1500, 270))
    gameDisplay.blit(subtract, coordToPixel((5,5), None))
    gameDisplay.blit(addition, coordToPixel((8,5), None))
    gameDisplay.blit(subtract, coordToPixel((5,8), None))
    gameDisplay.blit(addition, coordToPixel((8,8), None))
    gameDisplay.blit(subtract, coordToPixel((5,11), None))
    gameDisplay.blit(addition, coordToPixel((8,11), None))

    #Render ships
    gameDisplay.blit(cargo, (350, 405))
    gameDisplay.blit(galley, (350, 604))
    gameDisplay.blit(schooner, (350, 270))

    pygame.display.update()