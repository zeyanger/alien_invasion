import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示外星人的类"""
    def __init__(self, alien_settings, screen):
        """初始化外星人并设置其位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.alien_settings = alien_settings

        # 加载外星人图像，并设置其rect设置
        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()

        # 外星人初始位置在屏幕左上角附近
        self.rect.x = float(self.rect.width / 2)
        self.rect.y = float(self.rect.height / 2)

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)
