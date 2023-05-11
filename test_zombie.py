import unittest
from unittest.mock import Mock
from unittest.mock import patch, MagicMock
from main import Game
import pygame as pg
from zombie_game.bullet import Bullet
from zombie_game.settings import *


class TestGame(unittest.TestCase):

    def setUp(self):
        pg.init()
        self.game = Game()

    def test_load_flash_smoke(self):
        self.game.load_flash_smoke()
        self.assertNotEqual(len(self.game.gun_smoke), 0) #make sure that successfully load some smoke image
    
    def test_load_green_smoke(self):
        self.game.load_green_smoke()
        self.assertNotEqual(len(self.game.zombie_death_smoke), 0)
    
    def test_load_light_mask(self):
        self.game.load_light_mask()
        self.assertIsNotNone(self.game.light_mask)
    
    def test_load_sounds(self):
        self.game.load_sounds()
        self.assertNotEqual(len(self.game.sound_effects),0)
        self.assertNotEqual(len(self.game.weapon_sounds),0)
        self.assertNotEqual(len(self.game.zombie_moan_sounds),0)
        self.assertNotEqual(len(self.game.zombie_pain_sounds),0)
        self.assertNotEqual(len(self.game.zombie_die_sounds),0)
        self.assertNotEqual(len(self.game.player_die_sounds),0)
        self.assertNotEqual(len(self.game.player_pain_sounds),0)

        #to make sure that _add_sounds is called after calling load_sounds
    
        with patch.object(self.game,'_add_sounds') as mock_add_sounds:
            self.game.load_sounds()
            calls = len(self.game.weapon_sounds)+5
            self.assertEqual(mock_add_sounds.call_count,calls)

    #stubing
    def test_add_sounds(self):
        sounds = ['test1.ogg','test2.ogg']
        sound_list = []
        vol = 0.5

        #mock function: pg.mixer.Sound in pygame
        mock_sound1 = MagicMock()
        mock_sound2 = MagicMock()

        mock_sound1.get_volume.return_value = vol
        mock_sound2.get_volume.return_value = vol

        with patch('pygame.mixer.Sound', side_effect=[mock_sound1, mock_sound2]):
            self.game._add_sounds(sounds, sound_list, vol)
        
        self.assertEqual(len(sounds),len(sound_list))
        for s in sound_list: #make sure all volumn is set correctly
            self.assertEqual(s.get_volume(),vol)
    
    def tearDown(self):
        pg.quit()



    
    






# class TestBullet(unittest.TestCase):
#     def setUp(self):
#         pg.init()
#         self.game = pg.sprite.Group()
#         self.all_sprites = pg.sprite.Group()
#         self.bullets = pg.sprite.Group()
#         self.player = pg.sprite.Sprite()
#         self.player.weapon = "pistol"
#         self.game.all_sprites = self.all_sprites
#         self.game.bullets = self.bullets
#         self.game.player = self.player
#         self.game.dt = 1 / FPS
#         self.game.bullet_images = {"large": pg.Surface((10, 10))}
#         self.bullet = Bullet(self.game, (0, 0), pg.math.Vector2(1, 0))

#     def tearDown(self):
#         pg.quit()

#     def test_init(self):
#         self.assertIsInstance(self.bullet, pg.sprite.Sprite)
#         self.assertIn(self.bullet, self.all_sprites)
#         self.assertIn(self.bullet, self.bullets)
#         self.assertEqual(self.bullet.image, self.game.bullet_images[WEAPONS[self.player.weapon]['bullet_size']])
#         self.assertEqual(self.bullet.position, pg.math.Vector2(0, 0))
#         self.assertEqual(self.bullet.vel, pg.math.Vector2(WEAPONS[self.player.weapon]['bullet_speed'], 0))

#     def test_update(self):
#         self.bullet.update()
#         self.assertEqual(self.bullet.position, pg.math.Vector2(WEAPONS[self.player.weapon]['bullet_speed'], 0))

#     def test_collision_with_wall(self):
#         wall = pg.sprite.Sprite()
#         wall.rect = pg.Rect(0, 0, 10, 10)
#         self.game.walls = pg.sprite.Group(wall)
#         self.bullet.update()
#         self.assertNotIn(self.bullet, self.all_sprites)
#         self.assertNotIn(self.bullet, self.bullets)

if __name__ == '__main__':
    unittest.main()