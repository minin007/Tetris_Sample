import pygame
from settings import Setting

class Message:
    """设置一个适用于换行的文本类别"""
    size = Setting.fontsize
    def __init__(self, text):
        self.text = text
        self.color = Setting.help_msg_tcolor
        self.bg = None
        self.font = pygame.font.SysFont('simhei', Setting.fontsize)
        self.surface = self.font.render(self.text, True, self.color, self.bg)
        self.rect = self.surface.get_rect()
        self.msg_x = Setting.help_msg_x + 10
        self.msg_y = Setting.help_msg_y + 20
    def show_me(self, screen):
        screen.blit(self.surface, (self.msg_x, self.msg_y))

def cut_text(text, textList):
    """拆分文本"""
    #global textList
    global lineSpacing  # 行距
    lineSpacing = Message.size * 0.6
    for i in range(0, len(text) + 1):
        m = Message(text[0:i])
        if m.rect.width > Setting.help_msg_width - 40 or m.text[len(m.text)-3:len(m.text)-1] == 'nn':
            textList.append(text[0:i - 3])
            # if (Message.size + lineSpacing) * len(textList) > Setting.help_msg_height - 20: textList.remove(textList[0])
            # 上边一行主要解决超过窗口高度
            text = text[i - 1:len(text)]
            cut_text(text, textList)
            break
        if i == len(text) and m.rect.width <= Setting.help_msg_width - 40:
            textList.append(text[0:i])
            # if (Message.size + lineSpacing) * len(textList) > Setting.help_msg_height - 20: textList.remove(textList[0])      


def messageShow(screen, text):
    """将信息显示到屏幕"""
    
    textList = []
    cut_text(text, textList)
    for i in range(0, len(textList)):
        m = Message(textList[i])
        m.msg_x += 10
        m.msg_y += 10 + i * (Message.size + lineSpacing)
        m.show_me(screen)
