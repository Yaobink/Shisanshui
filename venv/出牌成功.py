# !/usr/bin/env python
# -*- coding:utf-8 -*-
import pygame
import 用户界面 as login_use
import 后端 as shisanshui
import 重新开局 as restart
def success_card(user_id):
    # 英文文本框demo
    pygame.init()
    pygame.display.set_caption("柯老板的十三水!")
    screen = pygame.display.set_mode((881, 468), 0, 32)  # 创建界面，设置窗口大小

    background = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\智能出牌.png")  # 获取背景图片位置

    mouse_old = pygame.image.load(r"C:\Users\18605\Desktop\素材\素材\鼠标箭头.png")#获取鼠标素材位置
    mouse_cursor=pygame.transform.scale(mouse_old, (10, 10))#缩放鼠标图片
    shisanshui.read_opengame()
    shisanshui.dfs_1(1, 1)#解决问题，深搜
    shisanshui.submit_ans=shisanshui.printf_ans()
    shisanshui.submitgame(shisanshui.submit_ans)#提交牌局
    shisanshui.init_start()
    while True:# 游戏主循环

        # screen.blit(text_box,(0,0))#将文本框画上去
        screen.blit(background, (0, 0))  # 将背景图画上去
        x, y = pygame.mouse.get_pos()  # 获得鼠标位置

        screen.blit(pygame.font.SysFont("微软雅黑", 40).render(shisanshui.prints1, True, (0, 0, 0)), (400, 300))
        screen.blit(pygame.font.SysFont("微软雅黑", 40).render(shisanshui.prints2, True, (0, 0, 0)), (400, 325))
        screen.blit(pygame.font.SysFont("微软雅黑", 40).render(shisanshui.prints3, True, (0, 0, 0)), (400, 350))
        pygame.display.update()  # 刷新画面

        for event in pygame.event.get(): # 判断用户是否点击了关闭按钮
            if event.type == pygame.QUIT:# 如果关闭，退出
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()  # 获得鼠标位置
                if 811 < x < 811 + 28 and 15 < y < 15 + 28:
                    login_use.login_use(user_id)
                if 329 < x < 329 + 211 and 394 < y < 394 + 40:
                    restart.restart(user_id)




