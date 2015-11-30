import pygame, sys, classes, random, TileC
from time import sleep, time

#a file that loads all the animation images to improve performance

player_idle = []
player_idle.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Idle__000.png") , (28,40)))
player_idle.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Idle__001.png") , (28,40)))
player_idle.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Idle__002.png") , (28,40)))
player_idle.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Idle__003.png") , (28,40)))
player_idle.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Idle__004.png") , (28,40)))
player_idle.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Idle__005.png") , (28,40)))
player_idle.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Idle__006.png") , (28,40)))
player_idle.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Idle__007.png") , (28,40)))
player_idle.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Idle__008.png") , (28,40)))
player_idle.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Idle__009.png") , (28,40)))


player_running = []
player_running.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Run__000.png") , (40,40)))
player_running.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Run__001.png") , (40,40)))
player_running.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Run__002.png") , (40,40)))
player_running.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Run__003.png") , (40,40)))
player_running.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Run__004.png") , (40,40)))
player_running.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Run__005.png") , (40,40)))
player_running.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Run__006.png") , (40,40)))
player_running.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Run__007.png") , (40,40)))
player_running.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Run__008.png") , (40,40)))
player_running.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Run__009.png") , (40,40)))

player_jumping = []
player_jumping.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Jump__000.png") , (40,40)))
player_jumping.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Jump__001.png") , (40,40)))
player_jumping.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Jump__002.png") , (40,40)))
player_jumping.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Jump__003.png") , (40,40)))
player_jumping.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Jump__004.png") , (40,40)))
player_jumping.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Jump__005.png") , (40,40)))
player_jumping.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Jump__006.png") , (40,40)))
player_jumping.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Jump__007.png") , (40,40)))
player_jumping.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Jump__008.png") , (40,40)))
player_jumping.append( pygame.transform.scale(pygame.image.load("img/playerAnimation/Jump__009.png") , (40,40)))


robot_walking = []
robot_walking.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Run (1).png') , (40,40)))
robot_walking.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Run (2).png') , (40,40)))
robot_walking.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Run (3).png') , (40,40)))
robot_walking.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Run (4).png') , (40,40)))
robot_walking.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Run (5).png') , (40,40)))
robot_walking.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Run (6).png') , (40,40)))
robot_walking.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Run (7).png') , (40,40)))
robot_walking.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Run (8).png') , (40,40)))

robot_idle = []
robot_idle.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Idle (1) - copy.png') , (40,40)))
robot_idle.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Idle (2).png') , (40,40)))
robot_idle.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Idle (3).png') , (40,40)))
robot_idle.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Idle (4).png') , (40,40)))
robot_idle.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Idle (5).png') , (40,40)))
robot_idle.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Idle (6).png') , (40,40)))
robot_idle.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Idle (7).png') , (40,40)))
robot_idle.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Idle (8).png') , (40,40)))
robot_idle.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Idle (9).png') , (40,40)))
robot_idle.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Idle (10).png') , (40,40)))

robot_dead = []
robot_dead.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Dead (1).png') , (40,40)))
robot_dead.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Dead (2).png') , (40,40)))
robot_dead.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Dead (3).png') , (40,40)))
robot_dead.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Dead (4).png') , (40,40)))
robot_dead.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Dead (5).png') , (40,40)))
robot_dead.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Dead (6).png') , (40,40)))
robot_dead.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Dead (7).png') , (40,40)))
robot_dead.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Dead (8).png') , (40,40)))
robot_dead.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Dead (9).png') , (40,40)))
robot_dead.append( pygame.transform.scale(pygame.image.load('img/robotAnimation/Dead (10).png') , (40,40)))

