import pygame.font


class Target:

    def __init__(self, ai_game):
        """初始化按钮的属性"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        # 设置按钮尺寸和其他属性
        self.width, self.height = 50, 200
        self.button_color = (0, 250, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 20)
        # 创建rect对象并使其位于右上角
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.right = self.rect.width
        self.rect.left = self.screen_rect.width - self.rect.width
        # 按钮的标签只用创建一次
        # target坐标
        self.y = float(self.rect.y)

    def _prep_msg(self,msg):
        """将smg渲染成图像,并使其在按钮上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def update(self):
        """向上或向下移动target"""
        self.y += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.y = self.y

    def draw_button(self):
        # 绘制一个用于颜色填充的按钮，在绘制文本
        self.screen.fill(self.button_color, self.rect)
        # self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_edges(self):
        """如果target位于屏幕边缘就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom > screen_rect.height or self.rect.top < 0:
            return True