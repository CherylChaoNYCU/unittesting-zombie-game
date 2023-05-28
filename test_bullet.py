import unittest
import pygame as pg
from unittest.mock import Mock
from unittest.mock import patch, MagicMock
from main import Game
from zombie_game.item import *
from zombie_game.player import *
from zombie_game.bullet import *  # Replace with the actual module and class name

class TestBullet(unittest.TestCase):

    def setUp(self):
        self.game = Game()  # Create a sprite group for testing
        self.game.player.position = (0,0)
        self.game.player.rect = pg.Rect(0, 0, 2, 2)
        self.game.items = pg.sprite.Group()
        
    #mock the uniform function so that it will always return 1.0
    @patch('zombie_game.bullet.uniform', return_value=1.0)
    def test_bullet_update(self, mock_uniform):
        
        print("Test for bullet.py:")
        #stubing pos , dir
        position = (1, 1)
        direction = pg.math.Vector2(1, 0)
        self.game.dt = 1/1000
        
        object_center = vector(1, 1)
        gun_item = Item(self.game,object_center,'shotgun')
        gun_item.rect= pg.Rect(0, 0, 2, 2)
        self.game.items.add(gun_item)

        self.game._collide_player_with_items()
    
        bullet = Bullet(self.game, position, direction)
        #stub WEAPONS bullet lifetime
        WEAPONS[self.game.player.weapon]['bullet_lifetime'] = -1
        bullet.spawn_time = -1
        bullet.kill = Mock()

        bullet.update()
        

        # Assert that the bullet's position is updated correctly
        expected_position = pg.math.Vector2(position) + direction * self.game.dt * WEAPONS[bullet.game.player.weapon]['bullet_speed'] * mock_uniform.return_value
        self.assertEqual(bullet.position, expected_position)
        self.assertEqual(bullet.rect.center, (1,1))


        #check the times self.kill() in bullet.py be called
        self.assertEqual(bullet.kill.call_count,2)

        print("\ttest bullet.py : OK")
    
    def test_bullet_key_error(self):

        '''
        For key error exception(no any weapon causes keyerror!)
        '''

        print('Test for KeyError in bullet.py:')
        position = (100, 100)
        direction = pg.math.Vector2(1, 0)
        self.game.dt = 1/1000

        bullet = Bullet(self.game, position, direction)
        self.game._collide_player_with_items()

        bullet.spawn_time = -1000
        bullet.kill = Mock()
        bullet.update()
        self.assertEqual(bullet.kill.call_count,1)

        print("\tKey_Error test completed : OK")



       




    # Add more test methods for other scenarios...

if __name__ == '__main__':#pragma: no cover
    unittest.main()
