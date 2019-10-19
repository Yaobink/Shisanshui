# !/usr/bin/env python
# -*- coding:utf-8 -*-
import pygame
import time
import json
import 后端 as shisanshui
class node:
    flower=0 #1234
    num=0  # 234567891011121314, A14
    def __init__(self,f,n):
        self.flower=f
        self.num=n

poker_1,poker_2,poker_3=[],[],[]    # 扑克牌分堆
for i in range(0,20):
    poker_1.append(node(0,0))
    poker_2.append(node(0, 0))
    poker_3.append(node(0, 0))

class TextBox:
    def __init__(self, w, h, x, y, surface, font=None, callback=None):
        """
        :param w:文本框宽度
        :param h:文本框高度
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
        self.__surface = surface
        if font is None:
            self.font = pygame.font.Font(None, 50)  # 使用pygame自带字体
        else:
            self.font = font

    def draw(self, dest_surf):
        text_surf = self.font.render(self.text, True, (191, 191, 191))
        dest_surf.blit(self.__surface, (self.x, self.y))
        dest_surf.blit(text_surf, (self.x +10 , self.y + (self.height - text_surf.get_height())),
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


def rank():
    # 英文文本框demo
    pygame.init()
    pygame.display.set_caption("柯老板的十三水!")
    screen = pygame.display.set_mode((881, 468), 0, 32)  # 创建界面，设置窗口大小

    background = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\排行榜背景.png")  # 获取背景图片位置

    mouse_old = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\鼠标箭头.png")#获取鼠标素材位置
    mouse_cursor=pygame.transform.scale(mouse_old, (10, 10))#缩放鼠标图片

    name1  ="hanhan"
    name2 = "hanhan"
    name3 = "hanhan"
    name4 = "hanhan"
    name5 = "hanhan"
    score1=str(999)
    score2 = str(999)
    score3 = str(999)
    score4 = str(999)
    score5 = str(999)
    id1=str(999)
    id2=str(999)
    id3=str(999)
    id4=str(999)
    id5=str(999)
    while True:# 游戏主循环
        # screen.blit(text_box,(0,0))#将文本框画上去
        screen.blit(background, (0, 0))  # 将背景图画上去
        screen.blit(pygame.font.SysFont("微软雅黑", 30).render(name1, True, (255, 255, 255)), (253, 110))
        screen.blit(pygame.font.SysFont("微软雅黑", 30).render(id1, True, (255, 255, 255)), (370, 110))
        screen.blit(pygame.font.SysFont("微软雅黑", 30).render(score1, True, (255, 255, 255)), (525, 110))

        screen.blit(pygame.font.SysFont("微软雅黑", 30).render(name2, True, (255, 255, 255)), (253, 184))
        screen.blit(pygame.font.SysFont("微软雅黑", 30).render(id2, True, (255, 255, 255)), (370, 184))
        screen.blit(pygame.font.SysFont("微软雅黑", 30).render(score2, True, (255, 255, 255)), (525, 184))

        screen.blit(pygame.font.SysFont("微软雅黑", 30).render(name3, True, (255, 255, 255)), (253, 255))
        screen.blit(pygame.font.SysFont("微软雅黑", 30).render(id3, True, (255, 255, 255)), (370, 255))
        screen.blit(pygame.font.SysFont("微软雅黑", 30).render(score3, True,(255, 255, 255)), (525, 255))

        screen.blit(pygame.font.SysFont("微软雅黑", 30).render(name4, True, (255, 255, 255)), (253, 326))
        screen.blit(pygame.font.SysFont("微软雅黑", 30).render(id4, True, (255, 255, 255)), (370, 326))
        screen.blit(pygame.font.SysFont("微软雅黑", 30).render(score4, True, (255, 255, 255)), (525, 326))

        screen.blit(pygame.font.SysFont("微软雅黑", 30).render(name5, True, (255, 255, 255)), (253, 393))
        screen.blit(pygame.font.SysFont("微软雅黑", 30).render(id5, True, (255, 255, 255)), (370, 393))
        screen.blit(pygame.font.SysFont("微软雅黑", 30).render(score5, True,(255, 255, 255)), (525, 393))

        x, y = pygame.mouse.get_pos()  # 获得鼠标位置
        pygame.display.update()  # 刷新画面
        for event in pygame.event.get(): # 判断用户是否点击了关闭按钮
            if event.type == pygame.QUIT:# 如果关闭，退出
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()  # 获得鼠标位置
                if 0 < x < 83 and 0 < y < 61:
                    login_use()


def history():
    # 英文文本框demo
    pygame.init()
    pygame.display.set_caption("柯老板的十三水!")
    screen = pygame.display.set_mode((881, 468), 0, 32)  # 创建界面，设置窗口大小
    background = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\历史游戏背景.png")  # 获取背景图片位置
    mouse_old = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\鼠标箭头.png")#获取鼠标素材位置
    mouse_cursor=pygame.transform.scale(mouse_old, (10, 10))#缩放鼠标图片
    message=shisanshui.history(3,1)
    print(message)
    data=message["data"]
    data=data.json()

    print(data)
    # id1 = "ID:"+str(message["data"]["card"])
    id2 = "ID:"+str(999)
    id3 = "ID:"+str(999)

    card1_1="$9 $Q *A"
    card1_2="#3 $3 *3 $K &K"
    card1_3="*5 *10 #10 $10 &10"
    card2_1="&3 *8 *J"
    card2_2="&5 *6 &7 &8 #9"
    card2_3="$2 $4 $6 $8 $Q"
    card3_1="#5 #J *A"
    card3_2="*3 &4 *10 $K &K"
    card3_3="$3 $6 $8 $9 $A"

    score1="score:"+"+1"
    score2="score:"+"-7"
    score3="score:"+"-99"
    while True:# 游戏主循环
        # screen.blit(text_box,(0,0))#将文本框画上去
        screen.blit(background, (0, 0))  # 将背景图画上去
        # screen.blit(pygame.font.SysFont("微软雅黑", 30).render(id1, True, (255, 255, 255)), (115, 120))
        # screen.blit(pygame.font.SysFont("微软雅黑", 30).render(card1_1, True, (255, 255, 255)), (115, 158))
        # screen.blit(pygame.font.SysFont("微软雅黑", 30).render(card1_2, True, (255, 255, 255)), (115, 197))
        # screen.blit(pygame.font.SysFont("微软雅黑", 30).render(card1_3, True, (255, 255, 255)), (115, 236))
        # screen.blit(pygame.font.SysFont("微软雅黑", 30).render(score1, True, (255, 255, 255)), (115, 280))
        #
        # screen.blit(pygame.font.SysFont("微软雅黑", 30).render(id2, True, (255, 255, 255)), (353, 120))
        # screen.blit(pygame.font.SysFont("微软雅黑", 30).render(card2_1, True, (255, 255, 255)), (353, 158))
        # screen.blit(pygame.font.SysFont("微软雅黑", 30).render(card2_2, True, (255, 255, 255)), (353, 197))
        # screen.blit(pygame.font.SysFont("微软雅黑", 30).render(card2_3, True, (255, 255, 255)), (353, 236))
        # screen.blit(pygame.font.SysFont("微软雅黑", 30).render(score2, True, (255, 255, 255)), (353, 280))
        #
        # screen.blit(pygame.font.SysFont("微软雅黑", 30).render(id3, True, (255, 255, 255)), (588, 120))
        # screen.blit(pygame.font.SysFont("微软雅黑", 30).render(card3_1, True, (255, 255, 255)), (588, 158))
        # screen.blit(pygame.font.SysFont("微软雅黑", 30).render(card3_2, True, (255, 255, 255)), (588, 197))
        # screen.blit(pygame.font.SysFont("微软雅黑", 30).render(card3_3, True, (255, 255, 255)), (588, 236))
        # screen.blit(pygame.font.SysFont("微软雅黑", 30).render(score3, True, (255, 255, 255)), (588, 280))
        x, y = pygame.mouse.get_pos()  # 获得鼠标位置
        pygame.display.update()  # 刷新画面
        for event in pygame.event.get(): # 判断用户是否点击了关闭按钮
            if event.type == pygame.QUIT:# 如果关闭，退出
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()  # 获得鼠标位置
                if 0 < x < 83 and 0 < y < 61:
                    login_use()

def restart():
    # 英文文本框demo
    pygame.init()
    pygame.display.set_caption("柯老板的十三水!")
    screen = pygame.display.set_mode((881, 468), 0, 32)  # 创建界面，设置窗口大小

    background = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\重新开局.png")  # 获取背景图片位置

    mouse_old = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\鼠标箭头.png")#获取鼠标素材位置
    mouse_cursor=pygame.transform.scale(mouse_old, (10, 10))#缩放鼠标图片


    while True:# 游戏主循环

        # screen.blit(text_box,(0,0))#将文本框画上去
        screen.blit(background, (0, 0))  # 将背景图画上去
        x, y = pygame.mouse.get_pos()  # 获得鼠标位置
        pygame.display.update()  # 刷新画面

        for event in pygame.event.get(): # 判断用户是否点击了关闭按钮
            if event.type == pygame.QUIT:# 如果关闭，退出
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()  # 获得鼠标位置
                if 811 < x < 811 + 28 and 15 < y < 15 + 28:
                    login_use()
                if 329 < x < 329 + 211 and 401 < y < 401 + 40:
                    shisanshui.init_end()
                    open()

def tijiao():

    screen.blit(pygame.font.SysFont("微软雅黑", 40).render(shisanshui.prints1, True, (0, 0, 0)), (400, 300))
    screen.blit(pygame.font.SysFont("微软雅黑", 40).render(shisanshui.prints2, True, (0, 0, 0)), (400, 325))
    screen.blit(pygame.font.SysFont("微软雅黑", 40).render(shisanshui.prints3, True, (0, 0, 0)), (400, 350))

def change(flower,num):
    x=(flower-0)*4+(num-2)
    str0='C:/Users/18605/Desktop/素材/素材/Resources/'
    str0+=str(x)+'.png'
    return str0


def choosecard():

    pygame.init()
    pygame.display.set_caption("柯老板的十三水!")
    screen = pygame.display.set_mode((881, 468), 0, 32)  # 创建界面，设置窗口大小
    background = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\智能出牌.png")  # 获取背景图片位置
    mouse_old = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\鼠标箭头.png")  # 获取鼠标素材位置
    mouse_cursor = pygame.transform.scale(mouse_old, (10, 10))  # 缩放鼠标图片

    for i in range(1,3+1):
        poker_1[i]=shisanshui.end_3[i]
    for i in range(1,5+1):
        poker_2[i]=shisanshui.end_2[i]
    for i in range(1, 5 + 1):
        poker_3[i] = shisanshui.end_1[i]

    po1=pygame.image.load(change(poker_1[1].flower,poker_1[1].num))
    po2 = pygame.image.load(change(poker_1[2].flower,poker_1[2].num))
    po3 = pygame.image.load(change(poker_1[3].flower,poker_1[3].num))

    po4 = pygame.image.load(change(poker_2[1].flower,poker_2[1].num))
    po5 = pygame.image.load(change(poker_2[2].flower,poker_2[2].num))
    po6 = pygame.image.load(change(poker_2[3].flower,poker_2[3].num))
    po7=pygame.image.load(change(poker_2[4].flower,poker_2[4].num))
    po8 = pygame.image.load(change(poker_2[5].flower,poker_2[5].num))

    po9 = pygame.image.load(change(poker_3[1].flower,poker_3[1].num))
    po10 = pygame.image.load(change(poker_3[2].flower,poker_3[2].num))
    po11 = pygame.image.load(change(poker_3[3].flower,poker_3[3].num))
    po12 = pygame.image.load(change(poker_3[4].flower,poker_3[4].num))
    po13 = pygame.image.load(change(poker_3[5].flower,poker_3[5].num))


    while True:  # 游戏主循环
        # screen.blit(text_box,(0,0))#将文本框画上去
        screen.blit(background, (0, 0))  # 将背景图画上去
        x, y = pygame.mouse.get_pos()  # 获得鼠标位置

        screen.blit(po1, (250, 175))  # 画扑克
        screen.blit(po2, (330, 175))  # 画扑克
        screen.blit(po3, (410, 175))  # 画扑克

        screen.blit(po4, (250, 232))  # 画扑克
        screen.blit(po5, (330, 232))  # 画扑克
        screen.blit(po6, (410, 232))  # 画扑克
        screen.blit(po7, (490, 232))  # 画扑克
        screen.blit(po8, (570, 232))  # 画扑克

        screen.blit(po9, (250, 290))  # 画扑克
        screen.blit(po10, (330, 290))  # 画扑克
        screen.blit(po11, (410, 290))  # 画扑克
        screen.blit(po12, (490, 290))  # 画扑克
        screen.blit(po13, (570, 290))  # 画扑克

        pygame.display.update()  # 刷新画面

        for event in pygame.event.get():  # 判断用户是否点击了关闭按钮
            if event.type == pygame.QUIT:  # 如果关闭，退出
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()  # 获得鼠标位置
                if 811 < x < 811 + 28 and 15 < y < 15 + 28:
                    login_use()
                if 329 < x < 329 + 211 and 401 < y < 401 + 40:
                    restart()


def opencard():
    # 英文文本框demo
    pygame.init()
    pygame.display.set_caption("柯老板的十三水!")
    screen = pygame.display.set_mode((881, 468), 0, 32)  # 创建界面，设置窗口大小
    background = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\发牌中.png")  # 获取背景图片位置
    mouse_old = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\鼠标箭头.png")#获取鼠标素材位置



    while True:# 游戏主循环

        # screen.blit(text_box,(0,0))#将文本框画上去
        screen.blit(background, (0, 0))  # 将背景图画上去
        x, y = pygame.mouse.get_pos()  # 获得鼠标位置
        pygame.display.update()  # 刷新画面

        for event in pygame.event.get(): # 判断用户是否点击了关闭按钮
            if event.type == pygame.QUIT:# 如果关闭，退出
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()  # 获得鼠标位置
                if 811 < x < 811 + 28 and 15 < y < 15 + 28:
                    login_use()
                if 329 < x < 329 + 211 and 401 < y < 401 + 40:
                    choosecard()


def open():#开始牌局
    # 英文文本框demo
    pygame.init()
    pygame.display.set_caption("柯老板的十三水!")
    screen = pygame.display.set_mode((881, 468), 0, 32)  # 创建界面，设置窗口大小
    background = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\开始牌局.png")  # 获取背景图片位置
    mouse_old = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\鼠标箭头.png")#获取鼠标素材位置
    mouse_cursor=pygame.transform.scale(mouse_old, (10, 10))#缩放鼠标图片
    while True:# 游戏主循环

        # screen.blit(text_box,(0,0))#将文本框画上去
        screen.blit(background, (0, 0))  # 将背景图画上去

        x, y = pygame.mouse.get_pos()  # 获得鼠标位置
        pygame.display.update()  # 刷新画面

        for event in pygame.event.get(): # 判断用户是否点击了关闭按钮
            if event.type == pygame.QUIT:# 如果关闭，退出
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()  # 获得鼠标位置
                if 811 < x < 811 + 28 and 15 < y < 15 + 28:
                    login_use()
                if 329 < x < 329 + 211 and 401 < y < 401 + 40:
                    timestart = time.clock()
                    shisanshui.init_start()
                    shisanshui.read_opengame()
                    shisanshui.dfs_1(1, 1)  # 解决问题，深搜
                    shisanshui.submit_ans = shisanshui.printf_ans()
                    shisanshui.submitgame(shisanshui.submit_ans)  # 提交牌局
                    timeend = time.clock()
                    print("used time:"+str(timeend-timestart))
                    choosecard()

def login_use():#用户界面
    global user_id
    pygame.init()
    pygame.display.set_caption("柯老板的十三水!")
    screen = pygame.display.set_mode((881, 468), 0, 32)  # 创建界面，设置窗口大小
    menu_background = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\主菜单背景.png")  # 主菜单界面
    menu_button_jryx = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\主菜单进入游戏按钮.png").convert_alpha()
    menu_button_cjfj = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\主菜单创建房间按钮.png").convert_alpha()
    menu_button_lsyx = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\主菜单历史游戏按钮.png").convert_alpha()
    menu_button_phb = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\主菜单排行榜按钮.png").convert_alpha()
    menu_button_exit = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\主菜单退出登录按钮.png").convert_alpha()
    mouse_old = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\鼠标箭头.png")#获取鼠标素材位置
    mouse_cursor=pygame.transform.scale(mouse_old, (10, 10))#缩放鼠标图片
    text = str(user_id)

    while True:# 游戏主循环

        # screen.blit(text_box,(0,0))#将文本框画上去

        screen.blit(menu_background, (0, 0))
        screen.blit(menu_button_jryx, (135, 109))
        screen.blit(menu_button_phb, (181, 396))
        screen.blit(menu_button_lsyx, (17, 396))
        screen.blit(menu_button_cjfj, (408, 109))
        screen.blit(menu_button_exit, (713, 9))
        screen.blit(pygame.font.SysFont("微软雅黑", 20).render(text, True, (255,255, 255)), (135, 13))
        x, y = pygame.mouse.get_pos()  # 获得鼠标位置

        pygame.display.update()  # 刷新画面

        for event in pygame.event.get(): # 判断用户是否点击了关闭按钮
            if event.type == pygame.QUIT:# 如果关闭，退出
                exit()
            if 396 < y < 396 + 72 and 17 < x < 17 + 158:
                menu_button_lsyx = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\主菜单历史游戏按钮半透明.png")
            else:
                menu_button_lsyx = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\主菜单历史游戏按钮.png")
            if 396 < y < 396 + 72 and 181 < x < 181 + 158:
                menu_button_phb = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\主菜单排行榜按钮半透明.png")
            else:
                menu_button_phb = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\主菜单排行榜按钮.png")
            if 109 < y < 109 + 251 and 135 < x < 135 + 162:
                menu_button_jryx = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\主菜单进入游戏按钮变大.png")
            else:
                menu_button_jryx = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\主菜单进入游戏按钮.png")

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()  # 获得鼠标位置
                if 135 < x < 135 + 165 and 109 < y < 109 + 251:
                    open()
                if 713 < x < 713 + 125 and 9 < y < 9 + 38:
                    login()
                if 181 < x < 181 + 158 and 396 < y < 396 + 72:
                    history()
                if 17 < x < 17 + 158 and 396 < y < 396 + 72:
                    rank()

def login():
    # 英文文本框demo
    global user_id
    pygame.init()
    pygame.display.set_caption("柯老板的十三水!")
    screen = pygame.display.set_mode((878, 465), 0, 32)  # 创建界面，设置窗口大小
    login_background = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\登录背景.png")  # 登录界面
    mouse_old = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\鼠标箭头.png")#获取鼠标素材位置
    mouse_cursor=pygame.transform.scale(mouse_old, (10, 10))#缩放图片
    flag1=0
    flag2=0
    textbox1=TextBox(259,45,361,137,pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\输入框.png"), callback=callback)
    textbox2=TextBox(259,45,361,199,pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\输入框.png"), callback=callback)
    textbox2fake=TextBox(259,45,361,199,pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\输入框.png"), callback=callback)
    while True:# 游戏主循环

        screen.blit(login_background, (0, 0))#画入登录界面
        textbox1.draw(screen)
        textbox2fake.text = ''.join(['·' * len(textbox2.text)])
        textbox2fake.draw(screen)
        x, y = pygame.mouse.get_pos()  # 获得鼠标位置
        pygame.display.update()  # 刷新画面

        for event in pygame.event.get(): # 判断用户是否点击了关闭按钮
            if event.type == pygame.QUIT:# 如果关闭，退出
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()  # 获得鼠标位置
                if 361<x<361+259 and 137<y<137+45:
                    flag1=1
                else:
                    flag1=0
                if 361<x<361+259 and 199<y<199+45:
                    flag2=1
                else:
                    flag2=0
                if 361 < x < 361 + 113 and 265 < y < 265 + 37 :
                    message=shisanshui.login("dzy007","dzy007")
                    user_id = message["data"]["user_id"]
                    login_use()
            elif event.type==pygame.KEYDOWN:
                if flag1 == 1:
                    textbox1.key_down(event)
                    pygame.time.delay(33)
                if flag2== 1:
                    textbox2.key_down(event)
                    pygame.time.delay(33)


login()