def Pirates():   
    ##GUI Main Game
    import pygame, time, sys
    gamePadCoordinate = ""

    def run_game():
        pygame.init()

        #black = (0, 0, 0)
        #white = (255, 255, 255)
        #red = (255, 0, 0)
        #green = (0, 255, 0)
        #blue = (0, 0, 255)
        background = (51, 70, 242)
        battlefieldBackground=pygame.image.load('./resources//images/background-battlefield.jpg')

        display_width = 1920
        display_height = 1080

        gameDisplay = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
        pygame.display.set_caption('Pirates PC!')
        clock = pygame.time.Clock()
        gameDisplay.fill(background)
        gameDisplay.blit(battlefieldBackground, (0,0))
        pygame.display.update()

        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()

            time.sleep(0.03)
    run_game()

Pirates()
