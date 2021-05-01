class Settings:
    """初始化游戏设置"""
    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_heigh = 800
        self.bg_color = (230, 230, 230)
        # 飞船设置
        self.ship_speed = 2
        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        # 外星人设置
        self.alien_speed = 1.0

