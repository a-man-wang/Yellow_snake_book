import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        # 窗口设置
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigh))
        # 全屏设置
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_heigh = self.screen.get_rect().height
        pygame.display.set_caption("Aline Invasion")
        self.ship = Ship(self)
        # 设置背景色
        # self.bg_color = (105, 139, 105)

    def _check_events(self):
        # 监听游戏和键盘事件
        for envent in pygame.event.get():
            if envent.type == pygame.QUIT:
                sys.exit()
            elif envent.type == pygame.KEYDOWN:
                self._check_keydown_events(envent)
            elif envent.type == pygame.KEYUP:
                self._check_keyup_events(envent)

    def _check_keydown_events(self,envent):
        """响应按下按键"""
        if envent.key == pygame.K_RIGHT:
            # 向右移动飞船
            self.ship.moving_right = True
        elif envent.key == pygame.K_LEFT:
            self.ship.moving_left = True
            
    def _check_keyup_events(self,envent):
        """响应弹起按键"""
        if envent.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif envent.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif envent.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        # 每次循环重绘屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
