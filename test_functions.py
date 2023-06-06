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
from zombie_game.board import *
from os import path
import os


class Testfunctions(unittest.TestCase):        
    def test_collide_hit_rect(self):
        one = Mock()
        two = Mock()
        one.hit_rect.colliderect = Mock(return_value=True)
        two.hit_rect = Mock()
        result = collide_hit_rect(one, two)
        
        self.assertTrue(result)
        

    def test_no_collision(self):
        one = Mock()
        two = Mock()
        one.hit_rect.colliderect = Mock(return_value=False)
        two.hit_rect = Mock()
        result = collide_hit_rect(one, two)
        
        self.assertFalse(result)


    def test_get_hit(self):
        character = MagicMock()
        get_hit(character)
        expected_alpha = list(chain([i for i in range(0, 255, 25)] * 2))
        
        self.assertEqual(list(character.damage_alpha), expected_alpha)
        self.assertTrue(character.damaged)

    def test_draw_player_health(self):
        self.game=Game()
        pg.mixer.pre_init(44100, 16, 1, 2048)
        pg.init()
        self.game.board = Board(SCREEN_WIDTH, SCREEN_HEIGHT)
        print(pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32))
        
        draw_player_health(pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32), 20, 10, 0.7)
        surface = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        self.assertIsNotNone(pg.draw.rect(surface, (0, 255, 0), pg.Rect(20, 10, 70, 20)))



   
if __name__ == "__main__":
    unittest.main()
