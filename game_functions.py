import sys

import pygame

from bullet import Bullet
from alien import Alien


def check_keydown_events(event, alien_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(alien_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(alien_settings, screen, ship, bullets):
        """创建一颗子弹，并将其加入编组bullets中"""
        if len(bullets) < alien_settings.bullets_allowed:
            new_bullet = Bullet(alien_settings, screen, ship)
            bullets.add(new_bullet)


def creat_fleet(alien_settings, screen, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可容纳多少外星人
    # 外星人间距等于外星人宽度
    alien = Alien(alien_settings, screen)
    alien_width = alien.rect.width
    alien_space_x = alien_settings.screen_width - 2 * alien_width
    alien_numbers_x = int(alien_settings.screen_width / (2 * alien_width))

    # 创建第一行外星人
    for alien_number in range(alien_numbers_x):
        # 创建一个外星人并将其加入当前行
        alien = Alien(alien_settings, screen)
        alien.x = float(alien_width / 2) + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)


def check_keyup_events(event, ship):
    """响应松开按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(alien_settings, screen, ship, bullets):
    # 响应鼠标和键盘事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, alien_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(alien_settings, screen, ship, aliens, bullets):
    """更新屏幕图像"""
    screen.fill(alien_settings.background_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # 绘制的屏幕可见
    pygame.display.flip()

def update_bullet(bullets):
    """更新子弹位置并删除已存在的子弹"""
    # 更新子弹的位置
    bullets.update()

    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

