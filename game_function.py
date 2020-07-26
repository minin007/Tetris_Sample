import sys
import pygame
import random
from shape import Shape, Pos
from set_text import messageShow
from settings import Setting
from pygame.sprite import Group

def check_events(screen, shape):
    """响应按键"""
    
    for event in pygame.event.get():
        # print(event.type)
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
            elif event.key == pygame.K_UP and Setting.stop_flag == False:
                shape.change()
            elif event.key == pygame.K_DOWN:
                Setting.down_flag = True
                pygame.time.set_timer(pygame.USEREVENT, 500)
            elif event.key == pygame.K_SPACE:
                Setting.space_flag = True
        
            
               
        # 松开按键
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                Setting.moving_right = False
            elif event.key == pygame.K_LEFT:
                Setting.moving_left = False
            elif event.key == pygame.K_DOWN:
                Setting.down_flag = False
                pygame.time.set_timer(pygame.USEREVENT, 1000)
            elif event.key == pygame.K_SPACE:
                Setting.space_flag = False
        elif event.type == pygame.USEREVENT and Setting.stop_flag == False:
            shape.down()
        elif event.type == pygame.USEREVENT + 1 and Setting.stop_flag == False:    
            shape.move()

def update_tetris(screen, shape):
    """更新下落方块"""    
    # shape.change()
    for now_pos in shape.shape:
        now_pos = Pos(now_pos) + shape.now_pos
        now_pos = ((now_pos[0]-1)*30+40, (now_pos[1] - 1)*30+50, Setting.square_size, Setting.square_size)
        pygame.draw.rect(screen, shape.tetris_color, now_pos)
        
def update_board(screen, shape):
    """更新版面状态"""    
    for shape_pos in shape.shape:
        now_pos = Pos(shape_pos) + shape.now_pos
        now_pos = Pos(now_pos) + (0, 4)
        next_pos = (shape_pos[1] + 1, shape_pos[0])    
        if Setting.board_pos[now_pos[1] + 1][now_pos[0]] == 1 and next_pos not in shape.shape:
            Setting.stop_flag = True
    if Setting.stop_flag and shape.now_pos[1] > 1:
        for now_pos_show in shape.shape:
            now_pos_show = Pos(now_pos_show) + shape.now_pos
            now_pos_show = Pos(now_pos_show) + (0, 4)
            Setting.board_pos[now_pos_show[1]][now_pos_show[0]] = 1
    for i in range(1, 11):
        if Setting.board_pos[6][i] == 1:
            Setting.end_flag = True    
    for i in range(1, 11):
        for j in range(5, 25):
            if Setting.board_pos[j][i] == 1:
                now_pos = ((i - 1)*30+40, (j - 5)*30+50, Setting.square_size, Setting.square_size)
                pygame.draw.rect(screen, Setting.tetris_color['b'], now_pos)


def update_screen(screen, shape):
    """更新屏幕以及提示信息"""
    screen.fill(Setting.screen_color)
    board_pos = [Setting.board_x, Setting.board_y, Setting.board_width, Setting.board_height]
    pygame.draw.rect(screen, Setting.board_color, board_pos,0)
    help_msg_pos = [Setting.help_msg_x, Setting.help_msg_y, Setting.help_msg_width, Setting.help_msg_height]
    pygame.draw.rect(screen, Setting.help_msg_bgcolor, help_msg_pos,0)
    messageShow(screen, Setting.help_msg)
    update_tetris(screen, shape)
    update_board(screen, shape)
    pygame.display.flip()

def creat_tetris():
    """生成一个Tetris"""
    
    new_shape = random.choice('-OLJSZT')
    return new_shape
    

def startgame(screen):
    """开始游戏"""
    startmsg_pos = (450, 550)
    start_msg = pygame.image.load('./source/开始.png')
    screen.blit(start_msg, startmsg_pos)
    pygame.display.flip()
    if Setting.end_flag:
        while True:
            for event in pygame.event.get():
                # print(event.type)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if mouse_x > 450 and mouse_x < 530 and mouse_y > 550 and mouse_y < 590:
                        Setting.end_flag = False
            if Setting.end_flag == False:
                break

def gameover(screen):
    """游戏结束"""
    endmsg_pos = (Setting.screen_width/2 - 200, Setting.screen_height/2 -50)
    gameover_msg = pygame.image.load('./source/gameover.png')
    screen.blit(gameover_msg, endmsg_pos)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            # print(event.type)
            if event.type == pygame.QUIT:
                Setting.stop_flag = True
                pygame.quit()
                sys.exit()
    