import pygame
from pygame.sprite import Sprite
from settings import Setting
from threading import Timer

class Shape(Sprite):
    """关于方块形状的类"""
    def __init__(self, name):
        """在初始位置创建一个方块"""
        super().__init__()
        self.settings = Setting
        self.name = name
        self.shape = Setting.shape[name]
        self.tetris_color = Setting.tetris_color[name]
        self.initial_speed = Setting.initial_speed
        self.now_pos = (5, 0)
        self.speed = self.initial_speed
        self.state = Setting.state
        
        # 在初始位置创建一个Tetris
        


    def down(self):
        """控制方块的移动"""
        if Setting.stop_flag:
            self.speed = 0
        elif Setting.down_flag:
            self.speed = 2
        else: self.speed = self.initial_speed
        self.now_pos = Pos(self.now_pos) + (0, 1)

    def move(self):
        if Setting.stop_flag:
            pass
        elif Setting.moving_left:
            self.now_pos = Pos(self.now_pos) + (-1, 0)
        elif Setting.moving_right:
            self.now_pos = Pos(self.now_pos) + (1, 0)
        
      

        
    def change(self):
        """改变方块的方向"""
        if Setting.stop_flag:
            pass
        elif self.name == '-':
            if self.state == 0:
                self.shape[0] = Pos(self.shape[0]) + (0, 0)
                self.shape[1] = Pos(self.shape[1]) + (-1, 1)
                self.shape[2] = Pos(self.shape[2]) + (-2, 2)
                self.shape[3] = Pos(self.shape[3]) + (1, -1)
                self.state += 1
            elif self.state == 1:
                self.shape[0] = Pos(self.shape[0]) + (0, 0)
                self.shape[1] = Pos(self.shape[1]) + (1, -1)
                self.shape[2] = Pos(self.shape[2]) + (2, -2)
                self.shape[3] = Pos(self.shape[3]) + (-1, 1)
                self.state = 0
        elif self.name == 'L':
            if self.state == 0:
                self.shape[0] = Pos(self.shape[0]) + (0, 0)
                self.shape[1] = Pos(self.shape[1]) + (1, -1)
                self.shape[2] = Pos(self.shape[2]) + (-1, 1)
                self.shape[3] = Pos(self.shape[3]) + (0, -2)
                self.state += 1
            elif self.state == 1:
                self.shape[0] = Pos(self.shape[0]) + (0, 0)
                self.shape[1] = Pos(self.shape[1]) + (1, 1)
                self.shape[2] = Pos(self.shape[2]) + (-1, -1)
                self.shape[3] = Pos(self.shape[3]) + (2, 0)
                self.state += 1
            elif self.state == 2:
                self.shape[0] = Pos(self.shape[0]) + (0, 0)
                self.shape[1] = Pos(self.shape[1]) + (-1, 1)
                self.shape[2] = Pos(self.shape[2]) + (1, -1)
                self.shape[3] = Pos(self.shape[3]) + (0, 2)
                self.state += 1
            elif self.state == 3:
                self.shape[0] = Pos(self.shape[0]) + (0, 0)
                self.shape[1] = Pos(self.shape[1]) + (-1, -1)
                self.shape[2] = Pos(self.shape[2]) + (1, 1)
                self.shape[3] = Pos(self.shape[3]) + (-2, 0)
                self.state = 0
        elif self.name == 'J':
            if self.state == 0:
                self.shape[0] = Pos(self.shape[0]) + (0, 0)
                self.shape[1] = Pos(self.shape[1]) + (1, -1)
                self.shape[2] = Pos(self.shape[2]) + (-1, 1)
                self.shape[3] = Pos(self.shape[3]) + (-2, 0)
                self.state += 1
            elif self.state == 1:
                self.shape[0] = Pos(self.shape[0]) + (0, 0)
                self.shape[1] = Pos(self.shape[1]) + (1, 1)
                self.shape[2] = Pos(self.shape[2]) + (-1, -1)
                self.shape[3] = Pos(self.shape[3]) + (0, -2)
                self.state += 1
            elif self.state == 2:
                self.shape[0] = Pos(self.shape[0]) + (0, 0)
                self.shape[1] = Pos(self.shape[1]) + (-1, 1)
                self.shape[2] = Pos(self.shape[2]) + (1, -1)
                self.shape[3] = Pos(self.shape[3]) + (2, 0)
                self.state += 1
            elif self.state == 3:
                self.shape[0] = Pos(self.shape[0]) + (0, 0)
                self.shape[1] = Pos(self.shape[1]) + (-1, -1)
                self.shape[2] = Pos(self.shape[2]) + (1, 1)
                self.shape[3] = Pos(self.shape[3]) + (0, 2)
                self.state = 0
        elif self.name == 'S':
            if self.state == 0:
                self.shape[0] = Pos(self.shape[0]) + (1, -1)
                self.shape[1] = Pos(self.shape[1]) + (0, 0)
                self.shape[2] = Pos(self.shape[2]) + (1, 1)
                self.shape[3] = Pos(self.shape[3]) + (0, 2)
                self.state += 1
            elif self.state == 1:
                self.shape[0] = Pos(self.shape[0]) + (-1, 1)
                self.shape[1] = Pos(self.shape[1]) + (0, 0)
                self.shape[2] = Pos(self.shape[2]) + (-1, -1)
                self.shape[3] = Pos(self.shape[3]) + (0, -2)
                self.state = 0
        elif self.name == 'Z':
            if self.state == 0:
                self.shape[0] = Pos(self.shape[0]) + (-1, 1)
                self.shape[1] = Pos(self.shape[1]) + (0, 0)
                self.shape[2] = Pos(self.shape[2]) + (1, 1)
                self.shape[3] = Pos(self.shape[3]) + (2, 0)
                self.state += 1
            elif self.state == 1:
                self.shape[0] = Pos(self.shape[0]) + (1, -1)
                self.shape[1] = Pos(self.shape[1]) + (0, 0)
                self.shape[2] = Pos(self.shape[2]) + (-1, -1)
                self.shape[3] = Pos(self.shape[3]) + (-2, 0)
                self.state = 0
        elif self.name == 'T':
            if self.state == 0:
                self.shape[0] = Pos(self.shape[0]) + (0, 0)
                self.shape[1] = Pos(self.shape[1]) + (1, -1)
                self.shape[2] = Pos(self.shape[2]) + (-1, 1)
                self.shape[3] = Pos(self.shape[3]) + (1, 1)
                self.state += 1
            elif self.state == 1:
                self.shape[0] = Pos(self.shape[0]) + (0, 0)
                self.shape[1] = Pos(self.shape[1]) + (1, 1)
                self.shape[2] = Pos(self.shape[2]) + (-1, -1)
                self.shape[3] = Pos(self.shape[3]) + (-1, 1)
                self.state += 1
            elif self.state == 2:
                self.shape[0] = Pos(self.shape[0]) + (0, 0)
                self.shape[1] = Pos(self.shape[1]) + (-1, 1)
                self.shape[2] = Pos(self.shape[2]) + (1, -1)
                self.shape[3] = Pos(self.shape[3]) + (-1, -1)
                self.state += 1
            elif self.state == 3:
                self.shape[0] = Pos(self.shape[0]) + (0, 0)
                self.shape[1] = Pos(self.shape[1]) + (-1, -1)
                self.shape[2] = Pos(self.shape[2]) + (1, 1)
                self.shape[3] = Pos(self.shape[3]) + (1, -1)
                self.state = 0
        else:
            print(self.name)

    def update(self):
        """更新方块的位置与方向"""
        self.down()

class Pos:
    """坐标运算"""
    def __init__(self, pos):
        self.len = len(pos)
        self.pos = pos
    def __add__(self, pair):
        if type(self.pos[0]) != int:
            return list((self.pos[i][0] + pair[0], self.pos[i][1] + pair[1]) for i in range(self.len))
        else:
            return list((self.pos[0] + pair[0], self.pos[1] + pair[1]))
