import unittest
from unittest.mock import Mock
from unittest.mock import patch, MagicMock
from main import Game
import pygame as pg
from itertools import chain
from zombie_game.zombie import *
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
        self.game.player.position = (0.5,0.5)
        self.game.player.hit_rect = pg.Rect(0.5, 0.5, 2, 2)
        self.game.zombies = pg.sprite.Group()
        



    @patch('main.random', return_value=0.4)
    def test_collide_zombie(self,mock_rand):
        
        '''case1 player.lives > 0'''
        print("Test for collide_zombie in main.py:")
        print("case1 player.lives > 0:")

        zbs1 = Zombie(self.game,0.1,0.1)
        zbs1.rect = pg.Rect(0.1, 0.1, 2, 2)
        zbs1.vel = vector(-1,1) #should be 0,0 after calling main
        self.game.zombies.add(zbs1)

        #stubing player.shield & damage
        #one hit -> shield = 100-50=-50
        self.game.player.shield = 100
        self.game.damage = 150
        track = pg.mixer.Sound(path.join(self.game.sounds_folder, 'die_test.wav'))
        track.set_volume(0.5)
        self.game.player_pain_sounds = []
        self.game.player_pain_sounds.append(track)

        
        self.game.player.lives = 1
        self.game.player_start_pos = (0,0)
        

        #for get_hit function
        test = [i for i in range(0, 255, 25)]


        self.game._collide_player_with_zombie()
        self.assertEqual(zbs1.vel,vector(0,0))
        self.assertEqual(self.game.player.lives,0)
        self.assertEqual(self.game.player.vel,vector(0,0))
        self.assertEqual(self.game.player.shield,PLAYER_SHIELD)
        self.assertEqual(self.game.player.damaged,True)
        #final if hits
        tmp = set(self.game.player.damage_alpha)
        test = set(test)
        p = self.game.player.position
        self.assertSetEqual(test,tmp)
        hits = pg.sprite.spritecollide(self.game.player, self.game.zombies, False, collide_hit_rect)
        self.assertEqual(p,self.game.player_start_pos+vector(KICKBACK,0).rotate(-hits[0].rotation))


        print("\ttest collide_zombie1 : OK")

        print("case2 player.lives < 0:")
        '''case2 player.lives < 0'''

        zbs2 = Zombie(self.game,0.2,0.2)
        zbs2.rect = pg.Rect(0.2, 0.2, 2, 2)
        zbs2.vel = vector(-1,1) #should be 0,0 after calling main
        self.game.zombies.add(zbs2)


        self.game.player.shield = -1
        self.game.menu.game_over = Mock()
        self.game._collide_player_with_zombie()
        self.assertEqual(self.game.playing,False)
        self.assertEqual(self.game.menu.game_over.call_count,2) #two zombies in items! gameover * 2



        print("\ttest collide_zombie2 : OK")



   






if __name__ == '__main__':#pragma: no cover
    unittest.main()