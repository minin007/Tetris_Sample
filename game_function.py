import sys
import pygame
import random
from shape import Shape, Pos
from set_text import messageShow
from settings import Setting
from threading import Timer

def check_events(screen, shape):
    """响应按键"""
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Setting.stop_flag = True
            pygame.quit()
            sys.exit()
        # 按下按键
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Setting.moving_right = True
            elif event.key == pygame.K_LEFT:
                Setting.moving_left = True
            elif event.key == pygame.K_UP:
                shape.change()
            elif event.key == pygame.K_DOWN:
                Setting.down_flag = True
            elif event.key == pygame.K_SPACE:
                Setting.space_flag = True
        elif event.type == pygame.USEREVENT:
            shape.down()
            
               
        # 松开按键
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                Setting.moving_right = False
            elif event.key == pygame.K_LEFT:
                Setting.moving_left = False
            elif event.key == pygame.K_DOWN:
                Setting.down_flag = False
            elif event.key == pygame.K_SPACE:
                Setting.space_flag = False

def update_tetris(screen, shape):
    """更新下落方块"""
    shape.move()    
    # shape.change()
    for now_pos in shape.shape:
        now_pos = Pos(now_pos) + shape.now_pos
        now_pos = (now_pos[0]*30+40, now_pos[1]*30+50, Setting.square_size, Setting.square_size)
        pygame.draw.rect(screen, shape.tetris_color, now_pos, 1)
        
    

def update_screen(screen, shape):
    """更新屏幕以及提示信息"""
    screen.fill(Setting.screen_color)
    board_pos = [Setting.board_x, Setting.board_y, Setting.board_width, Setting.board_height]
    pygame.draw.rect(screen, Setting.board_color, board_pos,0)
    help_msg_pos = [Setting.help_msg_x, Setting.help_msg_y, Setting.help_msg_width, Setting.help_msg_height]
    pygame.draw.rect(screen, Setting.help_msg_bgcolor, help_msg_pos,0)
    messageShow(screen, Setting.help_msg)
    update_tetris(screen, shape)
    pygame.display.flip()

def creat_tetris():
    """生成一个Tetris"""
    new_shape = random.choice('-OLJSZT')
    return new_shape

def startgame():
    """开始游戏"""
    pass

def gameover():
    """游戏结束"""
    