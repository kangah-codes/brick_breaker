def gameOver():
    global running
    global level
    if player.life <= 0:
        while running:
            score = levelText.font1.render(f"You  reached level {level}", True, (255,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
            try:
                screen.fill((0, 0, 0))

                screen.blit(game_over, (400 - game_over.get_width()/2, 100))
                screen.blit(score, (400 - (score.get_width()/2), 200))

                pygame.display.update()

                pygame.time.wait(2000)
                running = False
                refresh = True
                level = 0
                for brick in brickGroup:
                    brick.kill()
                mainMenu()

                clock.tick(20)

            except:
                pass
    else:
        while running:
            score = levelText.font1.render(f"You  reached level {level}", True, (255,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
            try:
                screen.fill((0, 0, 0))

                screen.blit(game_over, (400 - game_over.get_width()/2, 100))
                screen.blit(score, (400 - (score.get_width()/2), 200))

                pygame.display.update()

                pygame.time.wait(2000)
                running = False
                refresh = True
                mainMenu()

                clock.tick(20)

            except:
                pass
            level = 0
            for brick in brickGroup:
                brick.kill()
            mainMenu()