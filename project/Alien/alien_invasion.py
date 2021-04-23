import sys
import pygame


class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Aline Invasion")
        # 设置背景色
        self.bg_color = (105, 139, 105)

    def run_game(self):
        """开始游戏主循环"""
        while True:
            # 监听游戏和键盘事件
            for envent in pygame.event.get():
                if envent.type == pygame.QUIT:
                    sys.exit()
            # 每次循环重绘屏幕
            self.screen.fill(self.bg_color)
            # 让最近绘制的屏幕可见
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
