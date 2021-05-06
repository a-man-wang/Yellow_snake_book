class GanmeStats:
    """跟踪游戏统计信息"""
    def __init__(self, ai_ganme):
        """初始化统计信息"""
        self.settings = ai_ganme.settings
        self.reset_stats()
        self.game_active = False
        # 任何情况下都不应该重置最高得分
        self.high_score = 0

    def reset_stats(self):
        """初始化游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ships_limit
        self.score = 0
        self.level = 1