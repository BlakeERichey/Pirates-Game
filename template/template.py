# ##Template for a page
# import pygame
# import components.common

# from components.common import coordToPixel, isInt, isAdjacent, Node

# def rename(root):
#   pygame.init()
  
#   background = (51, 70, 242)
#   battlefieldBackground=pygame.image.load('./resources/images/background-battlefield.jpg')

#   display_width = 1920
#   display_height = 1080

#   #Set GUI Size and title
#   gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
#   pygame.display.set_caption('Pirates PC!')
#   clock = pygame.time.Clock()

#   #Check for events
#   while root.page=="rename":
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#           pygame.quit()
#           quit()

#         #Monitor when keyboard key is pressed
#         if event.type == pygame.KEYDOWN:
#           if event.key == pygame.K_ESCAPE:
#             pygame.quit()
#             exit()

#     gameDisplay.fill(background)
#     font = pygame.font.SysFont("Arial", 70, True)
#     text = font.render("Testing", True, [0, 0, 0], None)
#     gameDisplay.blit(text, (0,0))
#     pygame.display.update()