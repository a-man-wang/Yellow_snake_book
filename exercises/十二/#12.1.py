"""

练习12-1：蓝色天空 创建一个背景为蓝色的Pygame窗口。

"""

import pygame
import sys


class BlueScreen():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("bilibili")
        self.bg_color = (0, 0, 255)

    def run_game(self):
        while True:
            for envent in pygame.event.get():
                if envent.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()


if __name__ == '__main__':
    blue = BlueScreen()
    blue.run_game()