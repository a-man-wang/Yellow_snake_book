import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理飞船所有发射子弹的类"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        # 在(0,0)创建一个子弹的矩形，再设置其正确位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        # 储存小数表示子弹位置
        self.y = float(self.rect.y)

    def update(self, *args, **kwargs) -> None:
        """向上移动子弹"""
        self.y -= self.settings.bullet_speed
        # 更新子弹的rect位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)