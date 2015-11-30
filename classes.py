import pygame , TileC, animations, math
from random import randint
from time import sleep, time
from TileC import Tile

#super class for all othe created classes on this file
class BaseClass(pygame.sprite.Sprite):
    
    allsprites = pygame.sprite.Group()
    def __init__(self, x, y, width, height, image_string):

        pygame.sprite.Sprite.__init__(self)
        BaseClass.allsprites.add(self)
        self.image = pygame.image.load(image_string)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velx = 0
        self.vely = 0
        self.width = width
        self.height = height

    #destroys sprite
    def destroy(self, ClassName):
        ClassName.List.remove(self)
        BaseClass.allsprites.remove(self)
        del self
    #returns number as a string
    def __str__(self):
        return str(self.get_number())

    #returns number
    def get_number(self):
        
        return int((self.rect.x / self.width) + 1) + ((self.rect.y / self.height) * 26)

    #returns tile based on sprite number
    def get_tile(self):

        return Tile.get_tile(self.get_number())
    

#class defining the player
class Player(BaseClass):
    List = pygame.sprite.Group()
    going_right = True
    def __init__(self, x, y, width, height, image_string):

        BaseClass.__init__(self, x, y, width, height, image_string)
        Player.List.add(self)
        self.jumping = False
        self.go_down = False
        self.up = False
        self.cooldown = .3
        self.last = time()
        self.health = 100
        self.i = 0
        self.ji = 0
        self.flip = 0
        self.flipI = 0
        self.running = False
        self.type = Player

    #applies gravity to the player
    def calc_grav(self):
        if self.vely == 0:
            self.vely = 1
        else:
            self.vely += .55
        
        if self.rect.y >= 640 - 80 and self.vely >= 0:
            self.vely = 0
            self.rect.y = 640 - 80
   
    #defines player movement
    def motion(self, display_width, display_height):
        predicted = self.rect.x + self.velx

        if predicted < 0:
            self.velx = 0
        elif predicted + self.width > display_width:
            self.velx = 0
        
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x + self.width > display_width:
            self.rect.x = display_width - self.width
            
        self.rect.x += self.velx
    
    #defines properties of a jump
    def jump(self, display_height):
        self.rect.y += 2
        tile_hit_list = pygame.sprite.spritecollide(self, TileC.Tile.SolidList, False)
        self.rect.y-=2

        if len(tile_hit_list) > 0 or self.rect.y +40 >= 640:
            self.vely = -10
            self.jumping = False
            

#defines an enemy class
class Enemy(BaseClass):
    List = pygame.sprite.Group()
    score = 0
    def __init__(self, x, y, width, height, image_string, vel):
        BaseClass.__init__(self, x, y, width, height, image_string)
        Enemy.List.add(self)
        self.velx = vel
        self.health = 2
        self.going_right = True
        self.running = False
        self.i = 1
        self.pList = []
        self.last = time()
        self.cooldown = .8
        self.type = Enemy
        
    #applies gravity
    def calc_grav(self):
        if self.vely == 0:
            self.vely = 1
        else:
            self.vely += .55
        
        if self.rect.y >= 640 - 80 and self.vely >= 0:
            self.vely = 0
            self.rect.y = 640 - 80
            
    #defines movement
    def move(self, display_width):
        if self.running > 0:
            self.running = True
        if self.rect.x + self.width > display_width or self.rect.x < 0:
            self.image = pygame.transform.flip(self.image, True, False)
            self.velx = -self.velx

        self.rect.x += self.velx

        if self.velx > 0:
            self.going_right = True
            if self.i >= len(animations.robot_walking):
                self.i = 1
            self.image = animations.robot_walking[self.i-1]
            self.i += 1
        elif self.velx < 0:
            self.going_right = False
            if self.i >= len(animations.robot_walking):
                self.i = 1
            self.image = pygame.transform.flip(animations.robot_walking[self.i-1], True, False)
            self.i += 1
        else:
            if self.i >= len(animations.robot_idle):
                self.i = 1
            self.image = animations.robot_idle[self.i-1]
            self.i += 1
        
    #Enemy death logic
    @staticmethod
    def update_all(display_width):
        for enemy in Enemy.List:
            i = 0
            enemy.calc_grav()
            enemy.move(display_width)
            if enemy.health <= 0:
                
                enemy.velx = 0
                enemy.image = animations.robot_dead[9]

                enemy.destroy(enemy)
                Enemy.score += 10
                

#class defining a Boss
class Boss(BaseClass):
    List = pygame.sprite.Group()
    def __init__(self, x, y, width, height, image_string):
        BaseClass.__init__(self, x, y, width, height, image_string)
        Boss.List.add(self)
        self.velx = 1.4
        self.vely = 1.4
        self.cooldown = 1
        self.last = time()
        self.type = Boss
        self.health = 25

    #defines movement
    @staticmethod
    def move():
        for boss in Boss.List:
            
            boss.rect.x += boss.velx
            boss.rect.y += boss.vely
            if boss.rect.x <= 0:
                boss.velx = -(boss.velx)
            elif boss.rect.x + 300 >= 1200:
                boss.velx = -(boss.velx)

            if boss.rect.y <= 280:
                boss.vely = -(boss.vely)
            if boss.rect.y >= 420:
                boss.vely = -(boss.vely)

            if boss.health <= 0:
                boss.velx = 0
                boss.destroy(boss)
                Enemy.score += 100

    
#class defining the player's projectiles
class PlayerProjectile(BaseClass):

    List = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_string):
        BaseClass.__init__(self, x, y, width, height, image_string)
        PlayerProjectile.List.add(self)
        self.velx = 0
        self.type = PlayerProjectile
    
    #moves all projectiles
    @staticmethod
    def movement():

        for projectile in PlayerProjectile.List:
            projectile.rect.x += projectile.velx
            projectile.rect.y += projectile.vely

        for projectile in PlayerProjectile.List:
            if projectile.rect.x + projectile.width > 1040 or projectile.rect.x < 0:
                projectile.destroy(projectile)
                

#class defining enemy's projectiles
class EnemyProjectile(BaseClass):

    List = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_string):
        BaseClass.__init__(self, x, y, width, height, image_string)
        EnemyProjectile.List.add(self)
        self.velx = 0
        self.type = EnemyProjectile
    
    #moves all projectiles
    @staticmethod
    def movement():

        for projectile in EnemyProjectile.List:
            projectile.rect.x += projectile.velx
            projectile.rect.y += projectile.vely

        for projectile in EnemyProjectile.List:
            if projectile.rect.x + projectile.width > 1040 or projectile.rect.x < 0:
                projectile.destroy(projectile)
    
#class defining a menu item
class MenuItem(BaseClass):
    List = pygame.sprite.Group()
    def __init__(self, x, y, width, height, image_string):
        BaseClass.__init__(self, x, y, width, height, image_string)
        MenuItem.List.add(self)
        self.type = MenuItem

    #checks if an item was selected
    def is_mouse_selection(self, posx, posy):
        if (posx >= self.rect.x and posx <= self.rect.x + self.width) and \
            (posy >= self.rect.y and posy <= self.rect.y + self.height):
                return True
        return False
 










                
