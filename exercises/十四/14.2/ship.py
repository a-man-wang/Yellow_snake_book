import pygame


class Ship:
    """管理飞船的类"""
    def __init__(self,ai_game):
        """初始化飞船位置并设置其初始位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # 加载飞船图像并获得其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # 对于每一艘新飞船，都将其放在屏幕底部中央
        self.rect.midleft = self.screen_rect.midleft
        # 飞船属性x可以存小数
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        """根据moving_right标志符移动飞船"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1
        if self.moving_top and self.rect.top > 0:
            self.rect.y -= 1
        # 根据self.x的值更新rect对象
        # self.rect.x = self.x
        # self.rect.y = self.y

    def blitme(self):
        """在指定位置绘制飞机"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕底端居中"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
