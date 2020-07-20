import pygame
import sys
from settings import Setting
import game_function
from shape import Shape
from pygame.sprite import Group

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((Setting.screen_width, Setting.screen_height))
    pygame.display.set_caption("Tetris")
    new_shape = game_function.creat_tetris()
    shape = Shape(new_shape)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    pygame.time.set_timer(pygame.USEREVENT + 1, 100)
    # 时钟对象 控制帧率
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        if Setting.stop_flag:
            new_shape = game_function.creat_tetris()
            shape = Shape(new_shape)
            
        game_function.check_events(screen, shape)
        Setting.stop_flag = False
        game_function.update_screen(screen, shape)
        
run_game()
