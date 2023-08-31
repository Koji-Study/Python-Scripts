import time
import pygame
import random

pygame.init()
#初始化游戏界面的大小
screen_width, screen_height = 320, 240
screen = pygame.display.set_mode((screen_width, screen_height))
#给游戏起个标题
pygame.display.set_caption('接住你的太阳')
#设置背景图片，并调整至适应窗口大小
bg_img = pygame.image.load("bg.png")
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height))
#设置太阳的图片,并设置太阳的大小
sun_img = pygame.image.load("sun.png")
sun_img = pygame.transform.scale(sun_img, (20, 20))
#设置人物的图片
girl_img = pygame.image.load("girl.png")
girl_img = pygame.transform.scale(girl_img, (20, 20))


def sun_move():
    #设置太阳下落的速度
    speed = 5
    #小女孩运动的步长
    step = 10
    #太阳的初始位置
    sun_x = random.randint(0, screen_width - 20)
    sun_y = 0
    #小女孩的初始位置
    girl_x = 150
    girl_y = 220
    running = True
    #按键按下起作用
    key_pressed_a = False
    key_pressed_d = False
    while running:
        time.sleep(0.1)
        screen.blit(bg_img, (0, 0))
        #小女孩横向变化
        girl_x += step
        #小女孩的边界处理
        if girl_x >= 300:
            girl_x = 300
            print("girl到达右边边界")
        elif girl_x <= 0:
            girl_x = 0
            print("girl到达左边边界")
        screen.blit(girl_img, (girl_x, girl_y))
        screen.blit(sun_img, (sun_x, sun_y))
        #太阳纵向位移
        sun_y += speed
        #当图片有重合时表示接住太阳
        if sun_x + 20 > girl_x and sun_x < girl_x + 20 and sun_y + 20 > girl_y and sun_y < girl_y + 20:
            sun_y = 0
            sun_x = random.randint(0, screen_width - 20)
            print("接住太阳！，重新落下")
        #当太阳落到底部时，重新落下
        if sun_y >= 240:
            sun_y = 0
            sun_x = random.randint(0, screen_width - 20)
            print("未接到，sun重新落下")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print("w,上_down")
                elif event.key == pygame.K_s:
                    print("s,下_down")
                elif event.key == pygame.K_a:
                    print("a,左_down")
                    key_pressed_a = True
                elif event.key == pygame.K_d:
                    print("d,右_down")
                    key_pressed_d = True
                elif event.key == pygame.K_q:
                    running = False
                    print("q,退_down")
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    print("w,上_up")
                elif event.key == pygame.K_s:
                    print("s,下_up")
                elif event.key == pygame.K_a:
                    print("a,左_up")
                    key_pressed_a = False
                elif event.key == pygame.K_d:
                    print("d,右_up")
                    key_pressed_d = False
                elif event.key == pygame.K_q:
                    running = False
                    print("q,退")
        #按下a向左移动
        if key_pressed_a == True:
            step = -10
        #按下d向右移动
        elif key_pressed_d == True:
            step = 10
        #按键抬起后，不做位移
        else:
            step = 0
        pygame.display.update()


if __name__ == '__main__':
    sun_move()
