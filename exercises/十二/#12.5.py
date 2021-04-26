"""

练习12-4：火箭 编写一个游戏，它在屏幕中央显示一个火箭，而玩家可使用四个方向键上下左右移动火箭。请务必确保火箭不会移到屏幕外面。

"""

import pygame
import sys
from ico import Ico


class BlueScreen():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("bilibili")
        self.bg_color = (230, 230, 230)
        self.ico = Ico(self)
        self.font = pygame.font.Font(None,60)
        self.font_color = (0, 255, 0)
        self.bk_color = (0, 0, 128)
        self.text = "None"

    def _check_events(self):
        # 监听游戏和键盘事件
        for envent in pygame.event.get():
            if envent.type == pygame.QUIT:
                sys.exit()
            elif envent.type == pygame.KEYDOWN:
                self._check_keydown_events(envent)
                self.get_font(envent)
                self.print_font()
            elif envent.type == pygame.KEYUP:
                self._check_keyup_events(envent)

    def _check_keydown_events(self, envent):
        """响应按下按键"""
        if envent.key == pygame.K_RIGHT:
            # 向右移动飞船
            self.ico.moving_right = True
        elif envent.key == pygame.K_LEFT:
            self.ico.moving_left = True
        elif envent.key == pygame.K_UP:
            self.ico.moving_top = True
        elif envent.key == pygame.K_DOWN:
            self.ico.moving_bottom = True
        elif envent.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, envent):
        """响应弹起按键"""
        if envent.key == pygame.K_RIGHT:
            self.ico.moving_right = False
        elif envent.key == pygame.K_LEFT:
            self.ico.moving_left = False
        elif envent.key == pygame.K_UP:
            self.ico.moving_top = False
        elif envent.key == pygame.K_DOWN:
            self.ico.moving_bottom = False

    def _update_screen(self):
        # 每次循环重绘屏幕
        self.screen.fill(self.bg_color)
        self.ico.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def print_font(self):
        fontobj = pygame.font.Font("freesansbold.ttf", 32)
        print(self.text)
        self.text = fontobj.render(f"{self.text}", True, self.font_color, self.bk_color)
        textRectObj = self.text.get_rect()
        textRectObj.center = (200, 150)
        self.screen.blit(self.text, textRectObj)

    def get_font(self, envent):
        if envent.key <= 11000:
            self.text = chr(envent.key)

    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()
            self.print_font()
            self.ico.update()
            self._update_screen()


if __name__ == '__main__':
    blue = BlueScreen()
    blue.run_game()