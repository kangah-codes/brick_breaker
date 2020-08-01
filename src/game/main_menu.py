from .sprites import *
from .main import *


def mainMenu():
    player.gameOver = False
    global running
    running = True
    while running:
        #print(player.gameOver)
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        game()
                    if event.key == pygame.K_q:
                        running = False
           
            screen.fill((0, 0, 0))

            screen.blit(main_font, (118, 100))
            screen.blit(start, (400 - (start.get_width()/2), 200))
            screen.blit(quitg, (400 - (quitg.get_width()/2), 250))

            pygame.display.update()

            clock.tick(20)

        except pygame.error as e:
            if e == 'video system not initialized':
                pygame.quit()

        except Exception as e:
            print(e)
