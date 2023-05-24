import unittest
from unittest.mock import Mock
from unittest.mock import patch, MagicMock
from main import Game
import pygame as pg
from zombie_game.bullet import Bullet
from zombie_game.settings import *
from zombie_game.player import *
from zombie_game.item import *
from zombie_game.menu import *
from os import path
import os


class TestCollide(unittest.TestCase):

    def setUp(self):
        pg.init()
        self.items = []
        self.game = Game()

        print('setting up')
        self.player = self.game.player
        
        



    
    def test_collide_bonus(self):
        
        #coffee
        bonus_c = pg.sprite.Sprite()
        bonus_c.type = 'coffee'
        self.items.append(bonus_c)
        self.game.hit_test_bonus = self.items

        #water
        bonus_w = pg.sprite.Sprite()
        bonus_w.type = 'water'
        self.items.append(bonus_w)
        self.game.hit_test_bonus = self.items
        #stub shield value
        self.game.player.shield = 0


        #beer
        bonus_b = pg.sprite.Sprite()
        bonus_b.type = 'beer'
        self.items.append(bonus_b)
        self.game.hit_test_bonus = self.items
        #stub damage value
        self.game.damage = 10
        





        self.game._collide_player_with_bonus()
        #self.assertEqual(self.player.weapon,'shotgun')
        self.assertEqual(self.player.speed,300)
        self.assertEqual(self.player.shield,200)
        self.assertEqual(self.game.damage,5)
        self.assertEqual(self.game.player.bonus,'EXTRA STRENGTH')

        
        with patch.object(self.game,'get_bonus') as mock_get_bonus:
            self.game.hit_test_bonus = self.items
            self.game.player.shield = 0
            self.game._collide_player_with_bonus()
            
            self.assertEqual(mock_get_bonus.call_count,3)






 



    
    def tearDown(self):
        print('tearing down')
        #pg.quit()
        #del self.game




if __name__ == '__main__':
    unittest.main()