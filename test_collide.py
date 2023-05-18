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


class TestGame(unittest.TestCase):

    def setUp(self):
        pg.init()
        self.game = Game()

        #self.assertRaises(Exception,self.game.menu.game_intro())
        print('setting up')
        
        
        #testing for items, stubing: shotgun/pistol/ammo_small/key/id card/money
        self.player = self.game.player
        self.item_img = self.game.items_images
        

    #Should this be written in another class?
    def test_collide_items(self):
        
        #stub the players' shield
        #self.game._collide_player_with_items()

        #self.player.shield = 50
        try:
            self.game.menu.game_intro()
        except:
            print('continue')
            
        print('Testing Collision')
        
        #stubing hits
        hits = self.game.hit_test
        #print(hits)
        for hit in hits:
            print(hit.type)
            if hit.type == 'pistol':#
                self.assertIn('pistolll',self.player.all_weapons)
                self.assertEqual(self.player.weapon,'pistol')




    
    def tearDown(self):
        print('tearing down')
        #pg.quit()
        #del self.game




if __name__ == '__main__':
    unittest.main()