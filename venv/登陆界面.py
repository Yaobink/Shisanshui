# !/usr/bin/env python
# -*- coding:utf-8 -*-
import pygame
import 用户界面 as login_use
import 后端 as shisanshui

class TextBox:
    def __init__(self, w, h, x, y, font=None, callback=None):
        """
        :param w:文本框宽度
        :param h:文本框高as度
        :param x:文本框坐标
        :param y:文本框坐标
        :param font:文本框中使用的字体
        :param callback:在文本框按下回车键之后的回调函数
        """
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.text = ""  # 文本框内容
        self.callback = callback
        # 创建
        self.__surface = pygame.Surface((w, h))
        # 如果font为None,那么效果可能不太好，建议传入font，更好调节
        if font is None:
            self.font = pygame.font.Font(None, 32)  # 使用pygame自带字体
        else:
            self.font = font
    def draw(self, dest_surf):
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        dest_surf.blit(self.__surface, (self.x, self.y))
        dest_surf.blit(text_surf, (self.x, self.y + (self.height - text_surf.get_height())),
                       (0, 0, self.width, self.height))
    def key_down(self, event):
        unicode = event.unicode
        key = event.key
        # 退位键
        if key == 8:
            self.text = self.text[:-1]
            return
        # 切换大小写键
        if key == 301:
            return
        # 回车键
        if key == 13:
            if self.callback is not None:
                self.callback()
            return
        if unicode != "":
            char = unicode
        else:
            char = chr(key)

        self.text += char

def callback():
    print("回车测试")

def login():
    # 英文文本框demo
    pygame.init()
    pygame.display.set_caption("柯老板的十三水!")
    screen = pygame.display.set_mode((878, 465), 0, 32)  # 创建界面，设置窗口大小

    background = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\登录背景.png")  # 获取背景图片位置

    mouse_old = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\鼠标箭头.png")#获取鼠标素材位置
    mouse_cursor=pygame.transform.scale(mouse_old, (10, 10))#缩放图片
    text_box = TextBox(200, 30, 200, 200, callback=callback)# 创建文本框

    while True:# 游戏主循环

        # screen.blit(text_box,(0,0))#将文本框画上去
        screen.blit(background, (0, 0))  # 将背景图画上去
        x, y = pygame.mouse.get_pos()  # 获得鼠标位置
        pygame.display.update()  # 刷新画面

        for event in pygame.event.get(): # 判断用户是否点击了关闭按钮
            if event.type == pygame.QUIT:# 如果关闭，退出
                exit()
            elif event.type == pygame.KEYDOWN:
                text_box.key_down(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()  # 获得鼠标位置
                if 361 < x < 361 + 125 and 264 < y < 264 + 37 :
                    message=shisanshui.login("dzy007","dzy007")
                    user_id = message["data"]["user_id"]
                    print(user_id)
                    login_use.login_use(user_id)

            # text_box.draw(background)
            # pygame.display.flip()


login()
