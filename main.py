import logic
import pygame
import sys
pygame.init()



if __name__ == '__main__':  # main should never really be imported, but just in case
    simsize = 128
    windowsize = 1024
    startstate = 'startstates/ak94_gun.txt'
    
    # command line arguments
    if "-s" in sys.argv:
        simsize = int(sys.argv[sys.argv.index("-s") + 1])
    if "-w" in sys.argv:
        windowsize = int(sys.argv[sys.argv.index("-w") + 1])
    if "-i" in sys.argv:
        startstate = 'startstates/' + sys.argv[sys.argv.index("-i") + 1] + ".txt"


    # set up game
    gameboard = logic.GameBoard(simsize=simsize, windowsize=windowsize, startstate=startstate)
    animation_speed = 60
    pause = -1


    # set up display
    running = True
    disp = pygame.display.set_mode((windowsize, windowsize))
    pygame.display.set_caption(f"Conway's Game Of Life (speed: {animation_speed/60:.2g})")
    clock = pygame.time.Clock()


    # game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE: pause *= -1
                if event.key == pygame.K_LEFT: animation_speed = max(5, animation_speed - 5)
                if event.key == pygame.K_RIGHT: animation_speed = min(120, animation_speed + 5)
                
                # update title
                paused = "PAUSED - " if (pause == 1) else ""
                pygame.display.set_caption(f"{paused}Conway's Game Of Life (speed: {animation_speed/60:.3g})")

        
        if pause == -1:
            # draw cells
            disp.fill((0, 0, 0))
            cells = pygame.surfarray.make_surface(gameboard.pixelarray())
            disp.blit(cells, (0, 0))
            
            # update gamestate
            gameboard.update_board()
        
        # update screen
        pygame.display.update()
        clock.tick(animation_speed)
