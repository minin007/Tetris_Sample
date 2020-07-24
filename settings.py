import pygame
class Setting():
    """储存Tetris的所有设置"""
    
    shape = {'-':[(0, 0), (1, 0), (2, 0), (-1, 0)],
             'O':[(0, 0), (-1, 0), (0, 1), (-1, 1)],
             'L': [(0, 0), (-1, 0), (1, 0), (-1, 1)],
             'J': [(0, 0), (-1, 0), (1, 0), (1, 1)],
             'S': [(-1, 0), (0, 0), (0, -1), (1, -1)],
             'Z': [( 1, 0), (0, 0), (0, -1), (-1, -1)],
             'T': [(0, 0), (-1, 0), (1, 0), (0, -1)]}
    tetris_color = {'-': (50, 50, 50),
                    'O': (200, 0, 0),
                    'L': (0, 200, 0),
                    'J': (0, 0, 200),
                    'S': (150, 150, 0),
                    'Z': (0, 150, 150),
                    'T': (150, 0, 150),
                    'b': (200, 200, 200)}
    initial_speed = 1
    square_size = 29
    # 标志位
    state = 0
    moving_left = False
    moving_right = False
    down_flag = False
    space_flag = False
    stop_flag = False
    end_flag = False
    # 屏幕设置
    screen_width = 600
    screen_height = 700
    screen_color = (230, 230, 230)

    # 方块堆积版面设置
    board_width = 300
    board_height = 600
    board_color = (0, 0, 0)
    board_x = 40
    board_y = 50
    board_pos = []
    for i in range(25):
        board_pos.append([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
    board_pos.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    

    # 提示信息设置
    help_msg_x = 380
    help_msg_y = 150
    help_msg_width = 180
    help_msg_height = 200
    help_msg_bgcolor = (200, 200 ,200)
    help_msg_tcolor = (20, 20 ,20)
    fontsize = 10
    help_msg = '这是一个简单的Tetris游戏nn' \
               '按下回车开始游戏nn' \
               '您的得分nn' \
               '待续'