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
from zombie_game.zombie import *
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
        



    @patch('main.random', return_value=0.4)
    def test_collide_bullet_zombie(self,mock_rand):
        
        '''Stubing bullet and zombie groups'''
        print("Test for collide_bullet_with_zombie in main.py:")
        #suppose player get a weapon 'rifle
        self.player.weapon = 'rifle'
        self.player.accurate_shot = 1

        self.game.zombies = pg.sprite.Group()
        self.game.bullets = pg.sprite.Group()

        #append one zombie
        zombie1 = Zombie(self.game,0,0)
        zombie1.rect = pg.Rect(0, 0, 20, 20)
        zombie1.shield = 100
        self.game.zombies.add(zombie1)

        #append one bullet
        position = (10, 10)
        direction = pg.math.Vector2(1, 0)

        bullet1 = Bullet(self.game,position,direction)
        bullet1.rect = pg.Rect(10, 10, 20, 20)
        self.game.bullets.add(bullet1)

        self.game._collide_bullet_with_zombie()

        self.assertEqual(zombie1.shield,20) #shot by one bullet from rifle
        self.assertEqual(self.game.player.accurate_shot,2)
        self.assertEqual(zombie1.vel,vector(0,0))

        #get_hit check
        test_a = [i for i in range(0, 255, 25)]
        tmp = set(zombie1.damage_alpha)
        test_a = set(test_a)
        self.assertEqual(zombie1.damaged,True)
        self.assertSetEqual(test_a,tmp)
        
        


        

        print("\ttest collide_bullet_with_zombie : OK")


  



   






if __name__ == '__main__':#pragma: no cover
    unittest.main()