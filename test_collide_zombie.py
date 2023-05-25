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
    @patch('zombie_game.functions.get_hit', return_value=True)
    def test_collide_zombie(self,mock_rand,mock_hit):
        
        '''case1 player.lives > 0'''
        print("Test for collide_zombie in main.py:")
        print("case1 player.lives > 0:")

        zbs1 = pg.sprite.Sprite()
        zbs1.vel = vector(-1,1) #should be 0,0 after calling main
        self.items.append(zbs1)
        self.game.hit_test_zb = self.items

        #stubing player.shield & damage
        #one hit -> shield = 100-50=-50
        self.game.player.shield = 100
        self.game.damage = 150
        track = pg.mixer.Sound(path.join(self.game.sounds_folder, 'die_test.wav'))
        track.set_volume(0.5)
        self.game.player_pain_sounds = []
        self.game.player_pain_sounds.append(track)

        
        self.game.player.lives = 1
        self.game.player_start_pos = (5,5)
        

        #for get_hit function
        test = [i for i in range(0, 255, 25)]


        self.game._collide_player_with_zombie()
        self.assertEqual(zbs1.vel,vector(0,0))
        self.assertEqual(self.game.player.lives,0)
        self.assertEqual(self.game.player.vel,vector(0,0))
        self.assertEqual(self.game.player.position,vector(5,5))
        self.assertEqual(self.game.player.shield,PLAYER_SHIELD)
        self.assertEqual(self.game.player.damaged,True)
        #self.assertEqual(self.game.player.damage_alpha,True)

        print("\ttest collide_zombie1 : OK")

        print("case2 player.lives < 0:")
        '''case2 player.lives < 0'''

        zbs2 = pg.sprite.Sprite()
        self.items.append(zbs2)
        self.game.hit_test_zb = self.items

        #stubing player.shield & damage
        #one hit -> shield = 100-50=-50
        self.game.player.shield = -1
        self.game.menu.game_over = Mock()
        self.game._collide_player_with_zombie()
        self.assertEqual(self.game.playing,False)
        self.assertEqual(self.game.menu.game_over.call_count,2) #two zombies in items! gameover * 2

        #get_hit = Mock()
        self.assertEqual(mock_hit.call_count,3)

        print("\ttest collide_zombie2 : OK")



   






if __name__ == '__main__':
    unittest.main()