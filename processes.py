import pygame, sys, classes, random, TileC, animations
from time import sleep, time

#takes hardware input and responds. Also defines attack logic.
def processes(player, FPS, total_frames):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #player shooting
        if event.type == pygame.MOUSEBUTTONDOWN:
            now = time()
            if now - player.last >= player.cooldown:
                player.last = now
                p = classes.PlayerProjectile(player.rect.x, player.rect.y, 25, 11,"img/playerAnimation/Kunai.png")
                
                laser = pygame.mixer.Sound("sword swing.ogg")
                pygame.mixer.Sound.play(laser)
                mousex, mousey = pygame.mouse.get_pos()
                
                if classes.Player.going_right:
                    p.velx = 10
                else:
                    p.velx = -10
                    p.image = pygame.transform.flip(pygame.image.load("img/playerAnimation/Kunai.png"), True, False)

    keys = pygame.key.get_pressed()

    #player movement
    if keys[pygame.K_d]:
        player.running = True
        player.velx = 5
        classes.Player.going_right = True
        if player.i >= len(animations.player_running):
            player.i = 0
        player.image = animations.player_running[player.i]
        
        player.i += 1
        
    #player movement
    elif keys[pygame.K_a]:
        player.running = True
        classes.Player.going_right = False
        player.velx = -5
        if player.i >= len(animations.player_running):
            player.i = 0
        player.image = pygame.transform.flip(animations.player_running[player.i] , True, False)
        player.i += 1

    else:
        player.velx = 0
        player.running = False

    #player jump button
    if keys[pygame.K_SPACE]:
        try:
            x = player.rect.x
            x2 = player.rect.x + 40
            y = player.rect.y - 20
            tile =  TileC.Tile.get_tile_at(x,y)
            tile2 =  TileC.Tile.get_tile_at(x2,y)
            if tile.type == 'empty' and tile2.type == 'empty':
                if player.jumping == False:
                    player.jump(1040)
                    player.ji = 0
                    player.jumping = True
        except:
            pass
            


    #boss attack logic
    if len(classes.Boss.List)>0:
        for boss in classes.Boss.List:
            now = time()
            if now - boss.last >= boss.cooldown:
                boss.last = now
                laser = pygame.mixer.Sound("RetroLaser1.wav")
                pygame.mixer.Sound.play(laser)
                p = classes.EnemyProjectile(boss.rect.x + 150, boss.rect.y+64, 3, 3,"img/blue2.png")
                p.velx = -8
                p = classes.EnemyProjectile(boss.rect.x + 150, boss.rect.y+64, 3, 3,"img/blue2.png")
                p.velx = 8
                p = classes.EnemyProjectile(boss.rect.x + 150, boss.rect.y+64, 3, 3,"img/blue2.png")
                p.vely = 8
                p = classes.EnemyProjectile(boss.rect.x + 150, boss.rect.y+64, 3, 3,"img/blue2.png")
                p.vely = -8
                p = classes.EnemyProjectile(boss.rect.x + 150, boss.rect.y+64, 3, 3,"img/blue2.png")
                p.velx = 8
                p.vely = 8
                p = classes.EnemyProjectile(boss.rect.x + 150, boss.rect.y+64, 3, 3,"img/blue2.png")
                p.velx = -8
                p.vely = -8
                p = classes.EnemyProjectile(boss.rect.x + 150, boss.rect.y+64, 3, 3,"img/blue2.png")
                p.velx = 8
                p.vely = -8
                p = classes.EnemyProjectile(boss.rect.x + 150, boss.rect.y+64, 3, 3,"img/blue2.png")
                p.velx = -8
                p.vely = 8
                
    #enemy attack logic
    for enemy in classes.Enemy.List:
        if enemy.velx < 0:
            if (enemy.rect.x - 400 < player.rect.x and enemy.rect.x > player.rect.x) and (player.rect.y < enemy.rect.y + 60 and player.rect.y > enemy.rect.y - 20):
                now = time()
                if now - enemy.last >= enemy.cooldown:
                    enemy.last = now
                
                    p = classes.EnemyProjectile(enemy.rect.x, enemy.rect.y, 25, 11,"img/blue.png")
                    p.image = pygame.transform.flip(pygame.image.load("img/blue.png"), True, False)
                    laser = pygame.mixer.Sound("RetroLaser1.wav")
                    pygame.mixer.Sound.play(laser)
                    p.velx = -8
        
        elif enemy.velx > 0:
            if (enemy.rect.x + 400 > player.rect.x and player.rect.x > enemy.rect.x) and (player.rect.y < enemy.rect.y + 60 and player.rect.y > enemy.rect.y - 20):
                now = time()
                if now - enemy.last >= enemy.cooldown:
                    enemy.last = now
                    p = classes.EnemyProjectile(enemy.rect.x, enemy.rect.y, 25, 11,"img/blue.png")
                    laser = pygame.mixer.Sound("RetroLaser1.wav")
                    pygame.mixer.Sound.play(laser)
                    p.velx = 8

        elif enemy.velx == 0:
            if (player.rect.y < enemy.rect.y + 60 and player.rect.y > enemy.rect.y - 20) and (player.rect.x < enemy.rect.x -400 or (player.rect.x > enemy.rect.x and player.rect.x < enemy.rect.x +400)):
                now = time()
                if now - enemy.last >= enemy.cooldown:
                    enemy.last = now
                    p = classes.EnemyProjectile(enemy.rect.x, enemy.rect.y, 25, 11,"img/blue.png")
                    laser = pygame.mixer.Sound("RetroLaser1.wav")
                    pygame.mixer.Sound.play(laser)
                    p.velx = +8

#random enemy spawn
def spawn(FPS, total_frames):
    four = FPS * 4
    if total_frames % four == 0:
        r = random.randint(1,2)
        x = 1
        if r == 2:
            x = 1200 - 40
        enemy = classes.Enemy( x, 720 - 40, 40, 40,"img/enemy.jpg")

#defines collisions
def collisions(player):
    
    for enemy in classes.Enemy.List:
        enemy_proj = pygame.sprite.spritecollide(enemy, classes.PlayerProjectile.List, True)
        if len(enemy_proj) > 0:
            for hit in enemy_proj:
                enemy.health -= 1

    for boss in classes.Boss.List:
        enemy_proj = pygame.sprite.spritecollide(boss, classes.PlayerProjectile.List, True)
        if len(enemy_proj) > 0:
            for hit in enemy_proj:
                boss.health -= 1

    player_dead = pygame.sprite.spritecollide(player, classes.Enemy.List, True)
    if len(player_dead) > 0:
    
        player.health = 0

    player_dead = pygame.sprite.spritecollide(player, classes.Boss.List, True)
    if len(player_dead) > 0:
    
        player.health = 0

    
    player_hit = pygame.sprite.spritecollide(player, classes.EnemyProjectile.List, True)
    if len(player_hit) > 0:
        for hit in player_hit:
            player.health -= 25

    for proj in classes.PlayerProjectile.List:
        projectile_hit_wall = pygame.sprite.spritecollide(proj, TileC.Tile.SolidList, False)
        if len(projectile_hit_wall) > 0:
            for hit in projectile_hit_wall:
                classes.PlayerProjectile.destroy(proj, classes.PlayerProjectile)

    for proj in classes.EnemyProjectile.List:
        projectile_hit_wall = pygame.sprite.spritecollide(proj, TileC.Tile.SolidList, False)
        if len(projectile_hit_wall) > 0:
            for hit in projectile_hit_wall:
                classes.EnemyProjectile.destroy(proj, classes.EnemyProjectile)        

    #player collisions with walls         
    try:
        predicted = player.rect.x + 40 + player.velx
        if player.going_right:
            predicted = player.rect.x + 40 + player.velx
            if TileC.Tile.get_tile_at( predicted,player.rect.y + 2).type == 'solid' or TileC.Tile.get_tile_at( predicted,player.rect.y + 38).type == 'solid':
                player.velx = 0
        elif player.going_right == False:
            predicted = player.rect.x + player.velx
            if TileC.Tile.get_tile_at( predicted,player.rect.y + 2).type == 'solid' or TileC.Tile.get_tile_at( predicted,player.rect.y + 38).type == 'solid':
                player.velx = 0
    except:
        pass

        
    player.rect.y += player.vely
    
    tile_hit_list = pygame.sprite.spritecollide(player, TileC.Tile.SolidList, False)
    for tile in tile_hit_list:
        if player.vely > 0:
            player.rect.y = tile.top -40
            player.jumping = False
        elif player.vely < 0:
            player.rect.y  = tile.top + 40
        player.vely = 0
        

    #emeny collisions with walls
    for enemy in classes.Enemy.List:
        tile_hit_list = pygame.sprite.spritecollide(enemy, TileC.Tile.SolidList, False)
        for tile in tile_hit_list:
        
            if enemy.going_right:
                enemy.rect.x = enemy.rect.x -10
                enemy.velx = -enemy.velx
                enemy.image = pygame.transform.flip(enemy.image, True, False)
            elif enemy.going_right == False:
                enemy.rect.x = enemy.rect.x + 10
                enemy.velx = -enemy.velx
                enemy.image = pygame.transform.flip(enemy.image, True, False)
        
        enemy.rect.y += enemy.vely
    
        tile_hit_list = pygame.sprite.spritecollide(enemy, TileC.Tile.SolidList, False)
        for tile in tile_hit_list:
            if enemy.vely > 0:
                enemy.rect.y = tile.top -40
            elif enemy.vely < 0:
               enemy.rect.y  = tile.top + 40
            enemy.vely = 0

    #enemy re-routing at platform edges
    for enemy in classes.Enemy.List:
        if enemy.velx < 0:
            x = enemy.rect.x - 0
            y = enemy.rect.y + 60
            tile =  TileC.Tile.get_tile_at(x,y)           
            if tile.type == 'empty':
                enemy.velx = -enemy.velx
        if enemy.velx > 0:
            x = enemy.rect.x + 60
            y = enemy.rect.y + 60
            tile =  TileC.Tile.get_tile_at(x,y)           
            if tile.type == 'empty':
                enemy.velx = -enemy.velx

#defines the players animation states
def playerAnimation(player):
    
    if player.jumping == True:
        if player.ji >= len(animations.player_jumping):
            player.ji = len(animations.player_jumping) - 1
        if player.going_right:
            player.image = animations.player_jumping[player.ji]
        if player.going_right == False:
            player.image = pygame.transform.flip(animations.player_jumping[player.ji], True, False)
        player.ji += 1
            
    elif player.running == False:
        if player.i >= len(animations.player_idle):
            player.i = 0
        if player.going_right:
            player.image = animations.player_idle[player.i]
        if player.going_right == False:
            player.image = pygame.transform.flip(animations.player_idle[player.i], True, False)

        player.i += 1










        
        
