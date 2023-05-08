import unittest
from unittest.mock import Mock
from unittest.mock import patch

import pygame as pg
from zombie_game.bullet import Bullet
from zombie_game.settings import *


class TestBullet(unittest.TestCase):
    def setUp(self):
        pg.init()
        self.game = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.player = pg.sprite.Sprite()
        self.player.weapon = "pistol"
        self.game.all_sprites = self.all_sprites
        self.game.bullets = self.bullets
        self.game.player = self.player
        self.game.dt = 1 / FPS
        self.game.bullet_images = {"large": pg.Surface((10, 10))}
        self.bullet = Bullet(self.game, (0, 0), pg.math.Vector2(1, 0))

    def tearDown(self):
        pg.quit()

    def test_init(self):
        self.assertIsInstance(self.bullet, pg.sprite.Sprite)
        self.assertIn(self.bullet, self.all_sprites)
        self.assertIn(self.bullet, self.bullets)
        self.assertEqual(self.bullet.image, self.game.bullet_images[WEAPONS[self.player.weapon]['bullet_size']])
        self.assertEqual(self.bullet.position, pg.math.Vector2(0, 0))
        self.assertEqual(self.bullet.vel, pg.math.Vector2(WEAPONS[self.player.weapon]['bullet_speed'], 0))

    def test_update(self):
        self.bullet.update()
        self.assertEqual(self.bullet.position, pg.math.Vector2(WEAPONS[self.player.weapon]['bullet_speed'], 0))

    def test_collision_with_wall(self):
        wall = pg.sprite.Sprite()
        wall.rect = pg.Rect(0, 0, 10, 10)
        self.game.walls = pg.sprite.Group(wall)
        self.bullet.update()
        self.assertNotIn(self.bullet, self.all_sprites)
        self.assertNotIn(self.bullet, self.bullets)

if __name__ == '__main__':
    unittest.main()