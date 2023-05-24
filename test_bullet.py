import unittest
import pygame as pg
from unittest.mock import Mock
from unittest.mock import patch, MagicMock
from main import Game
from zombie_game.player import *
from zombie_game.bullet import *  # Replace with the actual module and class name

class TestBullet(unittest.TestCase):

    def setUp(self):
        self.game = Game()  # Create a sprite group for testing
        self.items = []
        print('setting up')
    #mock the uniform function so that it will always return 1.0
    @patch('zombie_game.bullet.uniform', return_value=1.0)
    def test_bullet_update(self, mock_uniform):
        
        #stubing pos , dir
        position = (100, 100)
        direction = pg.math.Vector2(1, 0)
        self.game.dt = 1/1000
        
        #print(uniform(0.9,1.1))

        #shotgun: suppose a user collided with a shotgun
        gun_item = pg.sprite.Sprite()
        gun_item.type = 'shotgun'
        self.items.append(gun_item)
        self.game.hit_test = self.items
        self.game._collide_player_with_items()
        self.game.player.rotation = 180

        



        
        bullet = Bullet(self.game, position, direction)
        #stub WEAPONS bullet lifetime
        WEAPONS[self.game.player.weapon]['bullet_lifetime'] = -1
        bullet.spawn_time = -1
        bullet.kill = Mock()

        bullet.update()
        

        # Assert that the bullet's position is updated correctly
        expected_position = pg.math.Vector2(position) + direction * self.game.dt * WEAPONS[bullet.game.player.weapon]['bullet_speed'] * mock_uniform.return_value
        self.assertEqual(bullet.position, expected_position)
        #self.assertEqual(bullet.rect.center, expected_position)


        expected_rotation = 180 -90
        self.assertEqual(bullet.game.player.rotation-90, expected_rotation)
        #check the times self.kill() in bullet.py be called
        self.assertEqual(bullet.kill.call_count,2)
       



    def tearDown(self):
        print('tearing down')

    # Add more test methods for other scenarios...

if __name__ == '__main__':
    unittest.main()
