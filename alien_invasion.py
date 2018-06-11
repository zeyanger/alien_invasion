import sys

import pygame
from pygame.sprite import Group
from Settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    alien_settings = Settings()
    screen = pygame.display.set_mode((alien_settings.screen_width,
                                      alien_settings.screen_height))
    pygame.display.set_caption('alien_invasion')
    # 创建一艘飞船
    ship = Ship(alien_settings, screen)
    # 创建一个存储子弹的编组
    bullets = Group()
    # 创建一个外星人编组
    aliens = Group()

    # 创建外星人群
    gf.creat_fleet(alien_settings, screen, aliens)

    # 开始游戏主循环
    while True:
        gf.check_events(alien_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullet(bullets)
        gf.update_screen(alien_settings, screen, ship, aliens, bullets)


run_game()
