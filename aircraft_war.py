#!/usr/bin/python
# coding: utf-8

'微信飞机大战'

import pygame
import sys
import time
import random
from pygame.locals import *
# import platform
# platform.architecture()


if __name__ == '__main__':
    # 初始化 pygame
    pygame.init()
    # 创建游戏窗口
    screen_width, screen_height = 480, 852
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
    pygame.display.set_caption('飞机大战')

    # 绘制背景图像
    # 1. 加载图像数据
    bg = pygame.image.load('./res/background.png')
    # 2. blit 绘制图像
    screen.blit(bg, (0, 0))
    # 3. update 更新屏幕显示
    pygame.display.update()

    # 绘制玩家的飞机
    hero = pygame.image.load('./res/hero1.png')
    screen.blit(hero, (150, 300))

    # 创建时钟对象
    clock = pygame.time.Clock()
    
    # 游戏循环，以为游戏的正式开始。
    i = 0
    # while True:
    #     clock.tick(6)
    #     print(i)
    #     i += 1
    #     pass

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()