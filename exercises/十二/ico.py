import pygame


class Ico:
    """kklt类"""
    def __init__(self,my_game):
        """初始化角色并设置初始位置"""
        self.screen = my_game.screen
        self.screen_rect = my_game.screen.get_rect()
        # 加载图形极其外接矩形
        self.image = pygame.image.load("images/ico.bmp")
        self.rect = self.image.get_rect()
        #新角色设置到 屏幕中央底部
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """指定位置绘制飞机"""
        self.screen.blit(self.image,self.rect)