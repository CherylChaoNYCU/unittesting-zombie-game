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
        self.zombs = []
        self.game = Game()
                
        self.player = self.game.player
        self.collide_harmless = 0
        self.item_img = self.game.items_images

    def fake_player_collide(self):
        if(len(self.zombs) == 0 or self.collide_harmless): 
            return False
        else: 
            return True


    
    def test_All_Zombie_Died_True(self): #predicate = True

        print('Test1 for all zombie died: TFF:T')
        
        'case1: {T,T,F} : T'

        self.game.zombies = []

        with patch("main.Game._collide_player_with_zombie", new_callable=Mock) as mock_collide_player_zombie:
            mock_collide_player_zombie.side_effect = self.fake_player_collide
            self.assertEqual(self.game._All_Zombie_Died(),True)
        
        print('\tTest1 done, Major: A')



        print('Test2 for all zombie died: FTT:T')

        'case2: {F,T,T} : T'

        for i in range(5):
            zmb = Zombie(self.game,0,0)
            zmb.shield = -1
            zmb.speed = 0
            zmb.damaged = True

            self.zombs.append(zmb)
        
        self.game.zombies = self.zombs
        self.collide_harmless = 1

        with patch("main.Game._collide_player_with_zombie", new_callable=Mock) as mock_collide_player_zombie:
            mock_collide_player_zombie.side_effect = self.fake_player_collide
            self.assertEqual(self.game._All_Zombie_Died(),True)
        
        print('\tTest2 done, Major: B/C')
    
    
    def test_All_Zombie_Died_False(self): #predicate = False

        print('Test3 for all zombie died: FFF:F')
        
        'case3: {F,F,F} : F'

        for i in range(3):
            zmb = Zombie(self.game,0,0)
            zmb.shield = 100
            zmb.speed = 10
            zmb.damaged = False

            self.zombs.append(zmb)
        
        self.game.zombies = self.zombs
        self.collide_harmless = 0


        with patch("main.Game._collide_player_with_zombie", new_callable=Mock) as mock_collide_player_zombie:
            mock_collide_player_zombie.side_effect = self.fake_player_collide
            self.assertEqual(self.game._All_Zombie_Died(),False)
        
        print('\tTest3 done, Major: A/B/C')




if __name__ == '__main__':
    unittest.main()