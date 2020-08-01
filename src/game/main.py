from .sprites import *
from config.settings import *
from .fading import *

player = Player()
ballGroup.add(Ball())

levelText = FadingText(f"Level {level}", [255,255,255], 64, .3)
showOnce = True
contRender = False

main_font = levelText.font.render("Brick Breaker", True, (255,255,255))
start = levelText.font1.render("Press A to start", True, (0,255,0))
quitg = levelText.font1.render("Press Q to quit", True, (255,0,0))

game_over = levelText.font.render("Game Over!", True, (255, 0 ,0))
score = levelText.font1.render(f"Your reached level {level}", True, (255,0,0))

def game():
    try:
        #pygame.mixer.pause()
        global running
        global showOnce
        global level
        global speed
        global color
        global contRender
        global refresh
        running = True
        switch = True

        while running:
            life = levelText.font1.render(f"Life: {player.life}", True, color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
            
            try:
                screen.fill((0, 0, 0))
                screen.blit(life, (0, 500 - life.get_height()))

                if player.life >= 3:
                    color = green
                elif player.life == 2:
                    color = orange
                else:
                    color = red

            except:
                pass

            player.update(player.dt)
            brickGroup.update()
            ballGroup.update(player)

            player.draw(screen)

            if showOnce:
                levelText.render()
                levelText.fade(screen, 300, 200)

                if levelText.alpha == 0:
                    showOnce = False

            try:
                brickGroup.draw(screen)
                ballGroup.draw(screen)
                pygame.display.update()

            except:
                pass

            
            if switch:
                refresh = True
                switch = False

            if refresh:
                for brick in brickGroup:
                    brick.kill()
                for i in range(800):
                    for y in range(level*40):
                        if i % 80 == 0 and y % 40 == 0:
                            brickGroup.add(Brick(i, y))
                refresh = False


            if len(brickGroup) == 0:
                #print(level)
                #print("lesser")
                levelText.alpha = 255
                contRender = True
                level += 1
                speed += 1
                player.speed -= 1.5
                player.life += 1
                ball = ballGroup.sprites()[0]
                ball.pos.x = 400 - ball.rect.width/2
                ball.pos.y = 400
                ball.yspeed += 2
                ball.xspeed += 2
                
                for i in range(800):
                    for y in range(level*40):
                        if i % 80 == 0 and y % 40 == 0:
                            brickGroup.add(Brick(i, y))
                
                levelText.text = f"Level {level}"
            
            #global contRender
            if contRender:
                levelText.render()
                levelText.fade(screen, 300, 200)

                if levelText.alpha <= 0:
                    contRender = False


            clock.tick(fps)

    except Exception as e:
        print(e)
