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
        for shape_pos in self.shape:
            now_pos = Pos(shape_pos) + self.now_pos
            now_pos = Pos(now_pos) + (0, 4)
            next_pos = (shape_pos[1] + 1, shape_pos[0])    
            if Setting.board_pos[now_pos[1] + 1][now_pos[0]] == 1 and next_pos not in self.shape:
                Setting.stop_flag = True
        if Setting.stop_flag and self.now_pos[1] > 1:
            for now_pos_show in self.shape:
                now_pos_show = Pos(now_pos_show) + self.now_pos
                now_pos_show = Pos(now_pos_show) + (0, 4)
                Setting.board_pos[now_pos_show[1]][now_pos_show[0]] = 1
        if Setting.stop_flag == False:
            
            self.now_pos = Pos(self.now_pos) + (0, 1)

    def move(self):
        '''左右移动及左右碰撞识别'''
        for shape_pos in self.shape:
            now_pos = Pos(shape_pos) + self.now_pos
            now_pos = Pos(now_pos) + (0, 4)
            next_pos = (shape_pos[1] + 1, shape_pos[0])    
            if Setting.board_pos[now_pos[1]][now_pos[0] - 1] == 1 and next_pos not in self.shape:
                Setting.moving_left = False
            if Setting.board_pos[now_pos[1]][now_pos[0] + 1] == 1 and next_pos not in self.shape:
                Setting.moving_right = False
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
        
        else:
            for i in range(2):
                for j in range(2):
                    turn_flag = self.to_turn(i, j)
            
                    if turn_flag == 4:
                        self.now_pos = Pos(self.now_pos) + (i, j)
                        for x in range(4): 
                            self.shape[x] = (-self.shape[x][1], self.shape[x][0])
                        break
                if turn_flag == 4:
                    break    
            
            for i in range(0, -2, -1):
                if turn_flag == 4:
                    break
                for j in range(2):
                        
                    turn_flag = self.to_turn(i, j)
                    
                    if turn_flag == 4:
                        self.now_pos = Pos(self.now_pos) + (i, j)
                        for x in range(4): 
                            self.shape[x] = (-self.shape[x][1], self.shape[x][0])
                        break
        turn_flag = 0
                        
                        
    def to_turn(self, i, j):
        turn_flag = 0
        for shape_pos in self.shape:
            new_shape_pos = (-shape_pos[1], shape_pos[0])
            new_pos = Pos(new_shape_pos) + self.now_pos
            new_pos = Pos(new_pos) + (0 + i, 4 + j)
            if (new_pos[0] > 0 and new_pos[0] < 11) and (Setting.board_pos[new_pos[1]][new_pos[0]] == 0 or new_shape_pos in self.shape):
                turn_flag += 1
        return turn_flag

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
