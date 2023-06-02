import unittest
from unittest.mock import Mock
from unittest.mock import patch, MagicMock
from main import Game
from os import path
from random import choice, random

from zombie_game.board import Board
from zombie_game.functions import quit_game, collide_hit_rect, draw_player_health, get_hit
from zombie_game.item import Item
from zombie_game.menu import Menu
from zombie_game.player import Player
from zombie_game.screen import Camera, TiledMap
from zombie_game.settings import *
from zombie_game.walls import Obstacle
from zombie_game.zombie import Zombie
class Map_img:
    def __init__(self):
        pass

    def get_rect(self):
        print("TTE")
        pass

class Fake_Tile_Object:
    name = ""
    x = y = width = height = 0
    def __init__(self, name, x, y, width, height):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        pass

class Fake_Objects:
    objects = ""
    def __init__(self, path):
        print("on")
        self.objects = path

class Fake_TiledMap:
    tmxdata = ""
    def __init__(self, path):
        print("DA")
        self.tmxdata = Fake_Objects(path)
        pass
    def make_map(self):
        print("adwa")
        return Map_img()

class TestMain_New(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        pass

    def fake_objects(self):
        print("YYYYYYYYY")
        return self.all_test

    def fake_Player(self, x, dont_care):
        print("A")
        self.tmp.append(int(x))
        pass

    def fake_Obstacle(self, x, dont_care, dont_care1, dont_care2):
        self.tmp.append(int(x))
        print("B")
        pass

    def fake_Zombie(self, x, dont_care):
        self.tmp.append(int(x))
        print("C")
        pass

    def fake_Item(self, dont_care, name):
        self.tmp.append(name)
        print("D")
        pass

    def fake_TiledMap(self, path):
        print("fake_TiledMap")
        return Fake_TiledMap(self.all_test)

    def test0_new(self):
        print("Test for new functions in main.py:")
        self.tmp = []
        self.all_test = [Fake_Tile_Object("player", 0, 0, 2, 2),#first round: general case
                        Fake_Tile_Object("wall", 1, 1, 2, 2),
                        Fake_Tile_Object("locked", 2, 2, 2, 2),
                        Fake_Tile_Object("locked_gun", 3, 3, 2, 2),
                        Fake_Tile_Object("locked_card", 4, 4, 2, 2),
                        Fake_Tile_Object("zombie", 5, 5, 2, 2),
                        Fake_Tile_Object("beer", 6, 6, 2, 2),
                        Fake_Tile_Object("water", 7, 7, 2, 2),
                        Fake_Tile_Object("coffee", 8, 8, 2, 2), 
                        Fake_Tile_Object("player", 0, 0, 0, 2),#second round: invalid case
                        Fake_Tile_Object("wall", 0, 0, 0, 2),
                        Fake_Tile_Object("locked", 0, 0, 0, 2),
                        Fake_Tile_Object("locked_gun", 0, 0, 0, 2),
                        Fake_Tile_Object("locked_card", 0, 0, 0, 2),
                        Fake_Tile_Object("zombie", 0, 0, 0, 2),
                        Fake_Tile_Object("beer", 0, 0, 0, 2),
                        Fake_Tile_Object("water", 0, 0, 0, 2),
                        Fake_Tile_Object("coffee", 0, 0, 0, 2),
                        Fake_Tile_Object("player", 0, 0, 2, 0),#third round: invalid case
                        Fake_Tile_Object("wall", 0, 0, 2, 0),
                        Fake_Tile_Object("locked", 0, 0, 2, 0),
                        Fake_Tile_Object("locked_gun", 0, 0, 2, 0),
                        Fake_Tile_Object("locked_card", 0, 0, 2, 0),
                        Fake_Tile_Object("zombie", 0, 0, 2, 0),
                        Fake_Tile_Object("beer", 0, 0, 2, 0),
                        Fake_Tile_Object("water", 0, 0, 2, 0),
                        Fake_Tile_Object("coffee", 0, 0, 2, 0),
                        Fake_Tile_Object("other", 87, 87, 87, 87),#4-th round: other cases
                        Fake_Tile_Object("other", 87, 87, 0, 87),
                        Fake_Tile_Object("other", 87, 87, 87, 0)]

        self.expected = [0, 1, 2, 3, 4, 5, "beer", "water", "coffee"]

        with patch("zombie_game.screen.TiledMap", new_callable=Mock) as mock_TiledMap:
            mock_TiledMap.side_effect = self.fake_TiledMap
            with patch("pytmx.pytmx.TiledMap.objects", new_callable=Mock) as mock_objects:
                mock_objects.side_effect = self.fake_objects
                with patch("zombie_game.player.Player", new_callable=Mock) as mock_Player:
                    mock_Player.side_effect = self.fake_Player
                    with patch("zombie_game.walls.Obstacle", new_callable=Mock) as mock_Obstacle:
                        mock_Obstacle.side_effect = self.fake_Obstacle
                        with patch('zombie_game.zombie.Zombie', new_callable=Mock) as mock_Zombie:
                            mock_Zombie.side_effect = self.fake_Zombie
                            with patch('zombie_game.item.Item', new_callable=Mock) as mock_Item:
                                mock_Item.side_effect = self.fake_Item
                                print("here")
                                self.game.new()
                                print("there")
                                self.assertEqual(self.tmp, self.expected)


        print("\ttest new : OK")
        pass



# class TestMain_Draw(unittest.TestCase):
#     def setUp(self):
#         self.game = Game()
#         pass

#     def test0_draw(sekf):
#         print("Test for draw functions in main.py:")


        # self.possible_i = Mock()
        # self.possible_i.side_effect = [0.56, 0.66, 0.76, 0.86]

        # with patch("zombie_game.menu.Menu.set_mob_limit", new_callable=Mock) as mock_set_mob_limit:
        #     mock_set_mob_limit.side_effect = self.fake_set_mob_limit
        #     with patch("zombie_game.menu.Menu.game_choose_character", new_callable=Mock) as mock_game_choose_character:
        #         mock_game_choose_character.side_effect = self.fake_game_choose_character
        #         with patch("zombie_game.menu.Menu.game_options", new_callable=Mock) as mock_game_options:
        #             mock_game_options.side_effect = self.fake_game_options
        #             with patch('zombie_game.menu.quit_game', new_callable=Mock) as mock_quit_game:
        #                 mock_quit_game.side_effect = self.fake_quit_game
        #                 zombie_game.functions.quit_game = Mock()
        #                 zombie_game.functions.quit_game.side_effect = self.fake_quit_game

        #                 self.entry_name_list = Mock()
        #                 self.entry_name_list.side_effect = ["game_choose_character", "game_options", "game_options", "quit_game"]

        #                 for i in range(4):
        #                     self.assertEqua


#         print("\ttest draw : OK")
#         pass


if __name__ == '__main__':
    unittest.main()