"""

练习12-2：游戏角色 找一幅你喜欢的游戏角色位图图像或将一幅图像转换为位图。创建一个类，将该角色绘制到屏幕中央，
并将该图像的背景色设置为屏幕背景色，或者将屏幕背景色设置为该图像的背景色。

"""
import pygame
import sys
from ico import Ico


class BlueScreen():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("bilibili")
        self.bg_color = (0, 0, 255)
        self.ico = Ico(self)

    def run_game(self):
        while True:
            for envent in pygame.event.get():
                if envent.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.ico.blitme()
            pygame.display.flip()


if __name__ == '__main__':
    blue = BlueScreen()
    blue.run_game()