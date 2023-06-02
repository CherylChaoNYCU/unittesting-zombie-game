import unittest
from unittest.mock import Mock
from unittest.mock import patch, MagicMock
from main import Game
import pygame as pg
from itertools import chain
from zombie_game.bullet import Bullet
from zombie_game.settings import *
from zombie_game.player import *
from zombie_game.item import *
from zombie_game.menu import *
from zombie_game.functions import *
from zombie_game.walls import *
from os import path
import os


class TestCollideZombie(unittest.TestCase):

    def setUp(self):
        pg.init()
        self.items = []
        self.game = Game()
        #self.get_hit_test = get_hit(self.game.player)
        
        #testing for items, stubing: shotgun/pistol/ammo_small/key/id card/money
        self.player = self.game.player
        self.item_img = self.game.items_images
        

    @patch('zombie_game.settings.pg.mixer.get_busy', return_value=True)
    @patch('zombie_game.settings.pg.mixer.stop', return_value=True)
    def test_collide_bullet_door(self,mock_get_busy,mock_mixer_stop):
        

        print("Test for collide_bullet_with_door in main.py:")

        self.game.destroyed = False
        self.player.rect.centery = 1000
        self.game.locked_rooms = pg.sprite.Group()
        self.game.bullets = pg.sprite.Group()


        locked_room_key_1 = Obstacle(self.game, 0,0,200,200)
        locked_room_key_1.rect= pg.Rect(0, 0, 20, 20)
        locked_room_key_1.kill = Mock(return_value=True)
        self.game.locked_rooms.add(locked_room_key_1)
        


        #append one bullet
        position = (10, 10)
        direction = pg.math.Vector2(1, 0)

        bullet1 = Bullet(self.game,position,direction)
        bullet1.rect = pg.Rect(10, 10, 20, 20)
        self.game.bullets.add(bullet1)

        self.game._collide_bullet_with_door()

        self.assertEqual(locked_room_key_1.kill.call_count,1) #shot by one bullet from rifle
        self.assertEqual(mock_get_busy.call_count,1) #shot by one bullet from rifle
        self.assertEqual(mock_mixer_stop.call_count,1) #shot by one bullet from rifle
        self.assertEqual(self.game.destroyed,True)

        


        

        print("\ttest collide_bullet_with_door : OK")


  



   






if __name__ == '__main__':#pragma: no cover
    unittest.main()