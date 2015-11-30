import pygame, classes

#draws text to the display
def text_to_screen(gameDisplay, textin, x, y, size = 15,
            color = (255, 255, 255)):

        text = str(textin)
        font = pygame.font.SysFont('Arial', size)
        text = font.render(text, True, color)
        gameDisplay.blit(text, (x, y))

        
#draws the health bar
def healthBar(gameDisplay, player):
        text_to_screen(gameDisplay, "HEALTH:", 10, 10)
        pygame.draw.rect(gameDisplay, (0,0,0),(64,14, 100,10))
        if player.health > 0:
                pygame.draw.rect(gameDisplay, (0,255,0),(64 ,14, player.health,10))
        
        
#draws the score and time
def score(gameDisplay, FPS, total_frames):
        text_to_screen(gameDisplay, int(total_frames/FPS), 980,30, 30)
        text_to_screen(gameDisplay, classes.Enemy.score, 980, 70, 30)
        text_to_screen(gameDisplay, "SCORE:", 840, 70, 30)
        text_to_screen(gameDisplay, "TIME:", 840, 30, 30)
