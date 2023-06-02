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
        self.game = Game()
        self.game.player.shield = 1
        self.game.player.speed = 10
        self.game.damage = 10
        self.game.player.position = (0,0)
        self.game.player.rect = pg.Rect(0, 0, 2, 2)
        self.game.bonus_items = pg.sprite.Group()

       
    def stub_bonus(self):
        idx=0
        for i in ['coffee','water','beer']:
            object_center = vector(0.1*idx , 0.1*idx)
            bonus = Item(self.game,object_center,i)
            bonus.rect = pg.Rect(0.1*idx,0.1*idx,2,2)
            self.game.bonus_items.add(bonus)
            idx+=1
        
    def test_collide_bonus(self):

        print("Test for collide_bonus in main.py:")


        self.stub_bonus()
        self.game._collide_player_with_bonus()
        
        #self.assertEqual(self.player.weapon,'shotgun')
        self.assertEqual(self.game.player.speed,300)
        self.assertEqual(self.game.player.shield,200)
        self.assertEqual(self.game.damage,5)
        self.assertEqual(self.game.player.bonus,'EXTRA STRENGTH')

        print("\ttest collide_bonus : OK")

        
        print("Test for get_bonus in main.py:")
        with patch.object(self.game,'get_bonus') as mock_get_bonus:
            self.stub_bonus()
            self.game.player.shield = 1
            self.game._collide_player_with_bonus()
            self.assertEqual(mock_get_bonus.call_count,3)
        print("\ttest get_bonus : OK")








if __name__ == '__main__':#pragma: no cover
    unittest.main()