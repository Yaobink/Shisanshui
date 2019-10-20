import pygame
import time
import json
import 后端 as shisanshui
import sys

shisanshui.login("","")
while 1:
    try:
        timestart = time.clock()
        shisanshui.init_start()
        shisanshui.read_opengame()
        shisanshui.dfs_1(1, 1)  # 解决问题，深搜
        shisanshui.submit_ans = shisanshui.printf_ans()
        shisanshui.submitgame(shisanshui.submit_ans)  # 提交牌局
        timeend = time.clock()
        print("used time:" + str(timeend - timestart))
        shisanshui.init_end()
    except IndexError:
        time().sleep(5)
