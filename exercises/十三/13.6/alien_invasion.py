import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GanmeStats
from time import sleep


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
        self.stats = GanmeStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # 设置背景色
        # self.bg_color = (105, 139, 105)

    def _ship_hit(self):
        """响应飞船被外星人撞到"""
        if self.stats.ships_left > 0:
            # 将飞船的ships_left减1
            self.stats.ships_left -= 1
            # 清空剩下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()
            # 创建一群新的外星人并将飞船放到屏幕底部的中央
            self._create_fleet()
            self.ship.center_ship()
            # 暂停0.5s
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _create_fleet(self):
        """创建外新人群"""
        # 创建一个外星人
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = available_space_x // (2 * alien_width)
        # 计算屏幕可容纳多少行外星人
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_heigh - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        # 创建外星人群
        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """创建一个外星人并放在当前行"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

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
        elif envent.key == pygame.K_q:
            sys.exit()
        elif envent.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _check_keyup_events(self, envent):
        """响应弹起按键"""
        if envent.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif envent.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_fleet_edges(self):
        """有外星人达到边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_kile_num(self):
        """杀死几个外星人上游戏结束"""
        if self.stats.kill_num >= 5:
            self.stats.game_active = False

    def _change_fleet_direction(self):
        """将整群外星人下移，并改变他们的运动方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _fire_bullet(self):
        """创建一颗子弹并将其加入编组bulltes中"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新子弹位置并删除消失子弹"""
        # 更新子弹位置
        self.bullets.update()
        # 删除消失子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """相应子弹和外星人碰撞"""
        # 检查是否有子弹击中了外星人
        # 如果有，就删除相应的子弹和外星人
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)
        self.stats.kill_num += len(collisions)
        if not self.aliens:
            # 删除现有的子弹并新建一群外星人
            self.bullets.empty()
            self._create_fleet()

    def _check_aliens_bottom(self):
        """检查是否有外星人到达了屏幕底端"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 像飞船被撞了一样处理
                self._ship_hit()
                break

    def _update_screen(self):
        # 每次循环重绘屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def _update_aliens(self):
        """更新外星人群中所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()
        # 检测外星人与飞船的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._check_kile_num()
            # print(len(self.bullets))
            self._update_screen()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
