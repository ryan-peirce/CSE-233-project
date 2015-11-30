import pygame, sys, func, animations
from classes import *
from processes import *
from TileC import *
pygame.init()
pygame.font.init()
pygame.mixer.init()

#define some colors
white = (255,255,255)
black = (0,0,0,)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#define tiles for tile map
TILE_SIZE = 40
display_width = 26  #1040
display_height = 16 #640

#set starting level, display size and caption
level = 0
gameDisplay = pygame.display.set_mode((display_width*TILE_SIZE,display_height*TILE_SIZE))
pygame.display.set_caption('Super Cool Kiler Guy 3: The Reckoning')

#set clock, FPS, and starting states
clock = pygame.time.Clock()
FPS = 30
total_frames = 0
paused = False
music = False
dead = False
complete = False

#Game Loop
while True:
        if level != 0 and level < 4:
                if paused == False and dead == False and complete == False:
                        processes(player, FPS, total_frames)
                        #spawn(FPS, total_frames)
                        collisions(player)
                        playerAnimation(player)
                        keys = pygame.key.get_pressed()
                        
                        if player.health <= 0:
                                dead = True
                        if len(Enemy.List) <= 0 and len(Boss.List) <= 0:
                                complete = True
                                
                        player.calc_grav()
                        player.motion(display_width*TILE_SIZE, display_height*TILE_SIZE)
                        PlayerProjectile.movement()
                        EnemyProjectile.movement()
                        Enemy.update_all(display_width*TILE_SIZE)
                        if len(Boss.List) > 0:
                                Boss.move()
                        total_frames += 1
                        
                        #draw to display
                        gameDisplay.blit(background, (0,0) )
                        BaseClass.allsprites.draw(gameDisplay)
                        Tile.draw_tiles(gameDisplay)
                        if len(Boss.List) > 0:
                                Boss.move()
                                Boss.List.draw(gameDisplay)
                        func.healthBar(gameDisplay, player)
                        func.score(gameDisplay, FPS, total_frames)
                        func.text_to_screen(gameDisplay, "LEVEL: " , 420, 20,40, (255,0,0))
                        func.text_to_screen(gameDisplay, level, 540, 20,40, (255,0,0))
                        
                        #update display
                        pygame.display.update()
            
                        if keys[pygame.K_ESCAPE]:
                                paused = True
                #pause logic
                elif paused == True:

                        resume = MenuItem(382,120, 276, 100, "img/start.png"  )
                        main_menu = MenuItem(382,240, 276, 100, "img/quit.png"  )
                        BaseClass.allsprites.draw(gameDisplay)
                        pygame.display.update()
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        mousex, mousey = pygame.mouse.get_pos()
                                        if resume.is_mouse_selection(mousex,mousey) == True:
                                                for item in MenuItem.List:
                                                        item.destroy(MenuItem)
                                                paused = False
                                                
                                        
                                        elif main_menu.is_mouse_selection(mousex,mousey) == True:
                                                for item in MenuItem.List:
                                                        item.destroy(MenuItem)
                                                        for sprite in BaseClass.allsprites:
                                                                BaseClass.destroy(sprite, sprite.type)
                                                                Tile.empty_tiles()
                                                paused = False
                                                
                                                pygame.mixer.music.load("menu.ogg")
                                                pygame.mixer.music.play(-1)

                                                level = 0
                        

                #Player dead logic
                elif dead == True:

                        restart = MenuItem(382,120, 276, 100, "img/restart.png"  )
                        main_menu = MenuItem(382,240, 276, 100, "img/quit.png"  )
                        BaseClass.allsprites.draw(gameDisplay)
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        mousex, mousey = pygame.mouse.get_pos()
                                        if restart.is_mouse_selection(mousex,mousey) == True:
                                                for item in MenuItem.List:
                                                        item.destroy(MenuItem)
                                                for sprite in BaseClass.allsprites:
                                                                BaseClass.destroy(sprite, sprite.type)
                                                                Tile.empty_tiles()
                                                dead = False
                                                pygame.mixer.music.load("menu.ogg")
                                                pygame.mixer.music.play(-1)
                                                level = 0
                                                
                                        
                                        elif main_menu.is_mouse_selection(mousex,mousey) == True:
                                                for item in MenuItem.List:
                                                        item.destroy(MenuItem)
                                                        for sprite in BaseClass.allsprites:
                                                                BaseClass.destroy(sprite, sprite.type)
                                                                Tile.empty_tiles()
                                                dead = False
                                                pygame.mixer.music.load("menu.ogg")
                                                pygame.mixer.music.play(-1)

                                                level = 0
                        pygame.display.update()

                #level complete logic
                elif complete == True:
                        grade = ''
                        final_score = int(120 - ((int(total_frames/FPS) * .1) * 2) - (100 - player.health))
                        if final_score >= 100:
                                final_score = 100
                                grade = 'A+'
                        elif final_score >= 90:
                                grade = 'A'
                        elif final_score >= 80:
                                grade = 'B'
                        elif final_score >= 70:
                                grade = 'C'
                        elif final_score >= 60:
                                grade = 'D'
                        else:
                                grade = 'E'

                        if final_score <= 0:
                                final_score = 0
                        
                        func.text_to_screen(gameDisplay, "Final score: " + str(final_score) + ", Grade: " + grade,  320, 120,40, (255,0,0))
                        continue_game = MenuItem(382,180, 276, 100, "img/continue.png"  )
                        main_menu = MenuItem(382,300, 276, 100, "img/quit.png"  )
                        BaseClass.allsprites.draw(gameDisplay)
                        pygame.display.update()
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        mousex, mousey = pygame.mouse.get_pos()
                                        if continue_game.is_mouse_selection(mousex,mousey) == True:
                                               for item in MenuItem.List:
                                                        item.destroy(MenuItem)
                                                        for sprite in BaseClass.allsprites:
                                                                BaseClass.destroy(sprite, sprite.type)
                                                                Tile.empty_tiles()
                                               complete = False
                                                
                                               pygame.mixer.music.load("menu.ogg")
                                               pygame.mixer.music.play(-1)

                                               level = 0
                                                
                                        
                                        elif main_menu.is_mouse_selection(mousex,mousey) == True:
                                                for item in MenuItem.List:
                                                        item.destroy(MenuItem)
                                                        for sprite in BaseClass.allsprites:
                                                                BaseClass.destroy(sprite, sprite.type)
                                                                Tile.empty_tiles()
                                                complete = False
                                                
                                                pygame.mixer.music.load("menu.ogg")
                                                pygame.mixer.music.play(-1)

                                                level = 0
                                                   
                    

        
        #level select        
        elif level == 4:
                gameDisplay.blit(background, (0,0) )
                func.text_to_screen(gameDisplay, "SUPER COOL KILLER GUY 3: THE RECKONING", 160, 50,40, (255,0,0))
                BaseClass.allsprites.draw(gameDisplay)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                mousex, mousey = pygame.mouse.get_pos()
                                if back.is_mouse_selection(mousex,mousey) == True:
                                        for item in MenuItem.List:
                                                item.destroy(MenuItem)
                                                for sprite in BaseClass.allsprites:
                                                        BaseClass.destroy(sprite, sprite.type)
                                                        Tile.empty_tiles()
                                        level = 0

                                if level1.is_mouse_selection(mousex,mousey) == True:
                                        for item in MenuItem.List:
                                                item.destroy(MenuItem)
                                                for sprite in BaseClass.allsprites:
                                                        BaseClass.destroy(sprite, sprite.type)
                                                        Tile.empty_tiles()
                                        
                                        pygame.mixer.music.load("level1.ogg")
                                        pygame.mixer.music.play(-1)
                                        invalids =   (360,334,308,282,256,230,204,205,206,207,208,232,258,284,310,336,
                                              362,338,257,258,259,309,310,311,361,362,329,330,331,332,371,
                                              372,373,347,348,374,327,370,386,391,392,393,394,395,396,397,398,
                                              399,400,401,402,403,404,405,406,407,260,312,363,364,388,390,286,234,
                                              408,409,410,411,412,413,414,415,416,417,328,333,194,195,196,197,198,235,1,79,105,131,157, 
                                              280,281,255,263,262,264,57,58,59,60,117,118,119,120,261,186,106,161,132,53,27,265,266,72,73,182)



                                        background = pygame.image.load("img/4.png")
                            

                                        player = Player(0, display_height*TILE_SIZE - 80, 40, 40, "img/player.png")
                                        e1 = Enemy(600, 440, 40, 40, "img/robotAnimation/Idle (1).png",2)
                                        e2 = Enemy(620, 560, 40, 40, "img/robotAnimation/Idle (1).png",3)
                                        e3 = Enemy(740, 440, 40, 40, "img/robotAnimation/Idle (1).png",1)
                                        e4 = Enemy(2, 320, 40, 40, "img/robotAnimation/Idle (1).png",0)
                                        e5 = Enemy(880, 260, 40, 40, "img/robotAnimation/Idle (1).png",1)
                                        e6 = Enemy(480, 260, 40, 40, "img/robotAnimation/Idle (1).png",1)
                                        e7 = Enemy(160, 80, 40, 40, "img/robotAnimation/Idle (1).png",2)
                                        e8 = Enemy(520, 160, 40, 40, "img/robotAnimation/Idle (1).png",3)
                                        e9 = Enemy(800, 40, 40, 40, "img/robotAnimation/Idle (1).png",1)

                                        TileC.Tile.total_tiles = 1
                                        classes.Enemy.score = 0
                                        total_frames = 0

                                        for y in range(0, gameDisplay.get_height(), TILE_SIZE):
                                                for x in range(0, gameDisplay.get_width(), TILE_SIZE):
                                                        if Tile.total_tiles in invalids:
                                                                Tile(x, y, 'solid')
                                                        else:
                                                                Tile(x, y, 'empty')
                                        level = 1

                                if level2.is_mouse_selection(mousex,mousey) == True:
                                        for item in MenuItem.List:
                                                item.destroy(MenuItem)
                                                for sprite in BaseClass.allsprites:
                                                        BaseClass.destroy(sprite, sprite.type)
                                                        Tile.empty_tiles()
                                        pygame.mixer.music.load("level2.ogg")
                                        pygame.mixer.music.play(-1)

                                        invalids =   (391,392,393,394,395,396,397,398,
                                                      399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,
                                                      339,340,341,342,343,344,345,346,347,348,273,299,325,351,377,288,390,267,246,247,
                                                      65,91,117,143,169,195,221,247,189,183,184,157,106,111,112,113,114,115,116,60,61,62
                                                        ,8,15,41,67,9,10,11,12,13,14,144,145,146,147,148,149,150,151,152,153,68,69,70,
                                                      71,72,73,74,75,76,77,78,104,130,156,182,208,234,260,286,312,338,364,198,199,200,201,202,203,204,
                                                      205,206,207,248,249,250,251,252,255,256,257,258,259,303,304,305,306,307,308,309,
                                                      329,354,355,356,357,358,359,360,361,313)

                                        background = pygame.image.load("img/8bit.jpg")
                                        player = Player(0, display_height*TILE_SIZE - 80, 40, 40, "img/player.png")
                                        e1 = Enemy(160,480 ,40 ,40 , "img/robotAnimation/Idle (1).png",2)
                                        e2 = Enemy(0,200 ,40 ,40 ,  "img/robotAnimation/Idle (1).png",0)
                                        e3 = Enemy(40,240 ,40 ,40 ,  "img/robotAnimation/Idle (1).png",0)
                                        e4 = Enemy(280,120 ,40 ,40 ,  "img/robotAnimation/Idle (1).png",3)
                                        e5 = Enemy(280,40 , 40 ,40 ,  "img/robotAnimation/Idle (1).png",0)
                                        e6 = Enemy(600,160 ,40 ,40 ,  "img/robotAnimation/Idle (1).png",2)
                                        e7 = Enemy(680,240 , 40 ,40 ,  "img/robotAnimation/Idle (1).png",2)
                                        e8 = Enemy(600,320 ,40 ,40 ,  "img/robotAnimation/Idle (1).png",1)
                                        e9 = Enemy(880,320 ,40 ,40 ,  "img/robotAnimation/Idle (1).png",1)
                                        
                                        e10 = Enemy(760,400 ,40 ,40 ,  "img/robotAnimation/Idle (1).png",1)
                                        e11 = Enemy(680,480 , 40 ,40 ,  "img/robotAnimation/Idle (1).png",0)
                                        e12 = Enemy(760,560 ,40 ,40 ,  "img/robotAnimation/Idle (1).png",2)
                                        e13 = Enemy(840,560 ,40 ,40 ,  "img/robotAnimation/Idle (1).png",3)
                                        



                                        TileC.Tile.total_tiles = 1
                                        classes.Enemy.score = 0
                                        total_frames = 0

                                        for y in range(0, gameDisplay.get_height(), TILE_SIZE):
                                                for x in range(0, gameDisplay.get_width(), TILE_SIZE):
                                                        if Tile.total_tiles in invalids:
                                                                Tile(x, y, 'solid')
                                                        else:
                                                                Tile(x, y, 'empty')
                                        level = 2

                                if level3.is_mouse_selection(mousex,mousey) == True:
                                        for item in MenuItem.List:
                                                item.destroy(MenuItem)
                                                for sprite in BaseClass.allsprites:
                                                        BaseClass.destroy(sprite, sprite.type)
                                                        Tile.empty_tiles()
                                        pygame.mixer.music.load("level3.ogg")
                                        pygame.mixer.music.play(-1)

                                        invalids =   (391,392,393,394,395,396,397,398,
                                                      399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,
                                                      365,366,367,368,369,370,371,372,339,340,341,342,343,344,313,314,315,316,287,288,289,
                                                      261,262,235,383,384,385,386,387,388,389,390,359,360,361,362,363,364,335,336,337,338,
                                                      310,311,312,285,286,288,260
                                                      )



                                        background = pygame.image.load("img/space.png")

                                        
                                        player = Player(360, 680, 40, 40, "img/player.png")
                                        b1 = Boss(600,360 ,300 ,128 , "img/boss.png")


                                        TileC.Tile.total_tiles = 1
                                        classes.Enemy.score = 0
                                        total_frames = 0

                                        for y in range(0, gameDisplay.get_height(), TILE_SIZE):
                                                for x in range(0, gameDisplay.get_width(), TILE_SIZE):
                                                        if Tile.total_tiles in invalids:
                                                                Tile(x, y, 'solid')
                                                        else:
                                                                Tile(x, y, 'empty')



                                        level = 3

                                                                
                pygame.display.update()

        #controls page
        elif level == 5:
                gameDisplay.blit(background, (0,0) )
                func.text_to_screen(gameDisplay, "SUPER COOL KILLER GUY 3: THE RECKONING", 160, 50,40, (255,0,0))
                BaseClass.allsprites.draw(gameDisplay)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                mousex, mousey = pygame.mouse.get_pos()
                                if back.is_mouse_selection(mousex,mousey) == True:
                                        for item in MenuItem.List:
                                                item.destroy(MenuItem)
                                                for sprite in BaseClass.allsprites:
                                                        BaseClass.destroy(sprite, sprite.type)
                                                        Tile.empty_tiles()
                                        level = 0
                func.text_to_screen(gameDisplay, "A " , 160, 200,40, (255,0,0))
                func.text_to_screen(gameDisplay, "D " , 240, 200,40, (255,0,0))
                func.text_to_screen(gameDisplay, "(Movement: A - left, D - right) " , 80, 240,26, (255,0,0))

                func.text_to_screen(gameDisplay, "SPACE BAR" , 430, 320,40, (255,0,0))
                func.text_to_screen(gameDisplay, "(Jump) " , 480, 360,26, (255,0,0))

                func.text_to_screen(gameDisplay, "MOUSE CLICK" , 780, 200,40, (255,0,0))
                func.text_to_screen(gameDisplay, "(Shoot) " , 840, 240,26, (255,0,0))

                func.text_to_screen(gameDisplay, "Kill all enemies to complete each level! " , 360, 410,26, (255,0,0))
                
                pygame.display.update()
    
        #title screen
        elif level == 0:
            if music == False:
                    pygame.mixer.music.load("menu.ogg")
                    pygame.mixer.music.play(-1)
                    music = True
            background = pygame.image.load("img/menu.jpg")
            player = Player(-10000, -10000, 40, 40, "img/player.png")
            start = MenuItem(382,120, 276, 100, "img/start.png"  )
            levels = MenuItem(382,240, 276, 100, "img/levels.png"  )
            controls = MenuItem(382,360, 276, 100, "img/controls.png"  )
            quit_game = MenuItem(382,480, 276, 100, "img/quit.png"  )
            

        
            gameDisplay.blit(background, (0,0) )
            func.text_to_screen(gameDisplay, "SUPER COOL KILLER GUY 3: THE RECKONING", 160, 50,40, (255,0,0))
            BaseClass.allsprites.draw(gameDisplay)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = pygame.mouse.get_pos()
                    if start.is_mouse_selection(mousex,mousey) == True:
                            pygame.mixer.music.load("level1.ogg")
                            pygame.mixer.music.play(-1)
                            for item in MenuItem.List:
                                    item.destroy(MenuItem)
                            
                            invalids =   (360,334,308,282,256,230,204,205,206,207,208,232,258,284,310,336,
                                      362,338,257,258,259,309,310,311,361,362,329,330,331,332,371,
                                      372,373,347,348,374,327,370,386,391,392,393,394,395,396,397,398,
                                      399,400,401,402,403,404,405,406,407,260,312,363,364,388,390,286,234,
                                      408,409,410,411,412,413,414,415,416,417,328,333,194,195,196,197,198,235,1,79,105,131,157, 
                                      280,281,255,263,262,264,57,58,59,60,117,118,119,120,261,186,106,161,132,53,27,265,266,72,73,182)



                            background = pygame.image.load("img/4.png")
                            

                            player = Player(0, display_height*TILE_SIZE - 80, 40, 40, "img/player.png")
                            e1 = Enemy(600, 440, 40, 40, "img/robotAnimation/Idle (1).png",2)
                            e2 = Enemy(620, 560, 40, 40, "img/robotAnimation/Idle (1).png",3)
                            e3 = Enemy(740, 440, 40, 40, "img/robotAnimation/Idle (1).png",1)
                            e4 = Enemy(2, 320, 40, 40, "img/robotAnimation/Idle (1).png",0)
                            e5 = Enemy(880, 260, 40, 40, "img/robotAnimation/Idle (1).png",1)
                            e6 = Enemy(480, 260, 40, 40, "img/robotAnimation/Idle (1).png",1)
                            e7 = Enemy(160, 80, 40, 40, "img/robotAnimation/Idle (1).png",2)
                            e8 = Enemy(520, 160, 40, 40, "img/robotAnimation/Idle (1).png",3)
                            e9 = Enemy(800, 40, 40, 40, "img/robotAnimation/Idle (1).png",1)

                            TileC.Tile.total_tiles = 1
                            classes.Enemy.score = 0
                            total_frames = 0

                            for y in range(0, gameDisplay.get_height(), TILE_SIZE):
                                    for x in range(0, gameDisplay.get_width(), TILE_SIZE):
                                            if Tile.total_tiles in invalids:
                                                    Tile(x, y, 'solid')
                                            else:
                                                    Tile(x, y, 'empty')
                            level = 1

                    if levels.is_mouse_selection(mousex,mousey) == True:
                            for item in MenuItem.List:
                                    item.destroy(MenuItem)
                            level1 = MenuItem(382,120, 276, 100, "img/level1.png"  )
                            level2 = MenuItem(382,240, 276, 100, "img/level2.png"  )
                            level3 = MenuItem(382,360, 276, 100, "img/level3.png"  )
                            back = MenuItem(382,480, 276, 100, "img/menu.png"  )

                            level = 4

                    if controls.is_mouse_selection(mousex,mousey) == True:
                            
                            for item in MenuItem.List:
                                    item.destroy(MenuItem)
                            back = MenuItem(382,480, 276, 100, "img/menu.png"  )

                            level = 5
                    if quit_game.is_mouse_selection(mousex,mousey) == True:
                            pygame.quit()
                            sys.exit()
                        
        #advance clock however many frames set by FPS
        clock.tick(FPS)
