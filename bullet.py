import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """关于飞船所发射子弹的类"""
    def __init__(self, alien_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super().__init__()
        self.screen = screen
        self.alien_settings = alien_settings

        # 在（0，0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, alien_settings.bullet_width,
                                alien_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        # 子弹的颜色和速度
        self.color = alien_settings.bullet_color
        self.speed_factor = alien_settings.bullet_speed_factor

    def update(self):
        """子弹向上移动"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
