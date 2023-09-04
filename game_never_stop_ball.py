import time
import pygame
import random

pygame.init()
#初始化游戏界面的大小
screen_width, screen_height = 320, 240
screen = pygame.display.set_mode((screen_width, screen_height))
#给游戏起个标题
pygame.display.set_caption('从不停歇的球')
#设置球的图片,并设置太阳的大小
ball_img = pygame.image.load("ball.png")
ball_img = pygame.transform.scale(ball_img, (20, 20))

def ball_move():
    #设置球的速度
    speed_x = 5
    speed_y = 5
    #球的初始位置
    ball_x = random.randint(0, screen_width - 20)
    ball_y = random.randint(0, screen_height - 20)
    running = True
    while running:
        time.sleep(0.1)
        #清除屏幕
        screen.fill((255, 255, 255))
        ball_x += speed_x
        ball_y += speed_y
        #通过改变小球的移动数值正负，来控制小球的移动反弹
        if ball_x < screen_width - 20 and ball_x > 0:
            speed_x = speed_x
        elif ball_x >= screen_width - 20 or ball_x <= 0:
            speed_x = -speed_x
        if ball_y < screen_height - 20 and ball_y > 0:
            speed_y = speed_y
        elif ball_y >= screen_height - 20 or ball_y <= 0:
            speed_y = -speed_y
        print(speed_x, speed_y)
        print(ball_x, ball_y)
        screen.blit(ball_img, (ball_x, ball_y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                    print("q,退")
        pygame.display.update()

if __name__ == '__main__':
    ball_move()
