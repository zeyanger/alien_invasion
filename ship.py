import pygame


class Ship:

    def __init__(self, alien_settings, screen):
        """初始化飞船"""
        self.screen = screen
        self.alien_settings = alien_settings

        """初始化飞船及其位置"""
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 将飞船初始位置定在屏幕底部中心
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 创建移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志控制飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.alien_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.alien_settings.ship_speed_factor
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.bottom -= 1
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += 1

        # 根据center更新rect对象
        self.rect.centerx = self.center
